"""
Prediction engine for academic performance.
Predicts semester_aktif + 1 (so if aktif=3, predict=4).
"""
from datetime import date
from .curriculum import (
    CURRICULUM, get_prodi_key, get_wajib_courses, get_pilihan_courses,
    get_max_sks_by_ipk, validate_prerequisites, get_completed_courses
)


def get_related_courses_avg(kode: str, riwayat_semester: list, prodi_key: str) -> float:
    """Calculate average grade from all completed courses (as general performance indicator)."""
    all_grades = []
    for sem_data in riwayat_semester:
        for nilai in sem_data.get("nilai_matkul", []):
            angka = nilai.get("nilai_angka")
            if angka is not None:
                all_grades.append(angka)
    return sum(all_grades) / len(all_grades) if all_grades else 0.0


def get_cohort_average(prodi_key: str, angkatan: int) -> float:
    """Calculate cohort average. For now, use a reasonable estimate based on prodi."""
    # Realistic cohort averages by prodi
    cohort_defaults = {
        "TI": 3.15,
        "AK": 3.20,
        "TM": 3.10,
        "AP": 3.18,
    }
    return cohort_defaults.get(prodi_key, 3.15)


def predict_course_grade(
    kode: str,
    wajib: bool,
    historical_ipk: float,
    related_courses_avg: float,
    cohort_avg: float,
    trend: float,
) -> dict:
    """Predict grade for a single course.

    Formula: 60% historical IPK + 40% related courses avg.
    Cohort avg hanya dipakai jika IPK mahasiswa di bawah cohort (tidak menarik ke bawah).
    """
    # Jika related_avg tersedia, gabungkan dengan IPK historis
    if related_courses_avg > 0:
        base = (historical_ipk * 0.6) + (related_courses_avg * 0.4)
    else:
        base = historical_ipk

    # Cohort hanya berpengaruh jika mahasiswa di bawah rata-rata cohort
    if historical_ipk < cohort_avg:
        base = base * 0.85 + cohort_avg * 0.15

    # Trend adjustment: tiap poin trend memberi dampak kecil
    trend_adjustment = max(-0.5, min(0.5, trend * 0.2))

    raw = base + trend_adjustment
    raw = max(0.0, min(4.0, raw))
    
    # Round to nearest grade point
    grade_points = [4.0, 3.5, 3.0, 2.5, 2.0, 1.0, 0.0]
    grade_letters = ["A", "AB", "B", "BC", "C", "D", "E"]
    
    closest = min(grade_points, key=lambda x: abs(x - raw))
    idx = grade_points.index(closest)
    letter = grade_letters[idx]
    
    # Confidence based on data availability and trend stability
    confidence = 70
    if related_courses_avg > 0:
        confidence += 10
    if abs(trend) < 0.3:
        confidence += 10
    if historical_ipk >= 3.0:
        confidence += 5
    
    confidence = min(95, confidence)
    
    return {
        "kode": kode,
        "prediksi_nilai_angka": round(raw, 2),
        "prediksi_nilai_huruf": letter,
        "confidence": confidence,
    }


def build_sks_scenario(
    nim: str,
    prodi_key: str,
    semester_target: int,
    all_courses_predicted: list,
    target_sks: int,
    current_ipk: float,
    cumulative_sks_so_far: int,
) -> dict:
    """
    Build a SKS scenario by selecting courses optimally:
    - Always include all wajib courses
    - Add electives with best predicted grades, trying to hit target_sks exactly
    - If exact match not possible, pick the closest achievable (prefer <=target)
    """
    wajib_courses = [c for c in all_courses_predicted if c["wajib"]]
    pilihan_courses = [c for c in all_courses_predicted if not c["wajib"]]

    selected = list(wajib_courses)
    current_sks = sum(c["sks"] for c in selected)

    # If wajib already meets or exceeds target, just return wajib
    if current_sks >= target_sks:
        selected_courses = selected
    else:
        # Sort pilihan by predicted grade descending
        pilihan_sorted = sorted(
            pilihan_courses,
            key=lambda c: c["prediksi_nilai_angka"],
            reverse=True
        )
        # Try to reach target_sks exactly; if a course would overshoot,
        # try to find a smaller one first
        remaining_pilihan = list(pilihan_sorted)
        while remaining_pilihan and current_sks < target_sks:
            needed = target_sks - current_sks
            # Find best course that fits exactly
            exact_fit = next(
                (c for c in remaining_pilihan if c["sks"] == needed), None
            )
            if exact_fit:
                selected.append(exact_fit)
                current_sks += exact_fit["sks"]
                remaining_pilihan.remove(exact_fit)
                break
            # Find best course that fits (sks <= needed)
            fits = [c for c in remaining_pilihan if c["sks"] <= needed]
            if fits:
                # Take best-graded fitting course
                best = fits[0]
                selected.append(best)
                current_sks += best["sks"]
                remaining_pilihan.remove(best)
            else:
                # All remaining courses are larger than needed; take the best one (will overshoot)
                best = remaining_pilihan[0]
                selected.append(best)
                current_sks += best["sks"]
                remaining_pilihan.remove(best)
                break
        selected_courses = selected

    actual_sks = sum(c["sks"] for c in selected_courses)

    # Predict IPS for this scenario
    if actual_sks > 0:
        pred_ips = sum(c["prediksi_nilai_angka"] * c["sks"] for c in selected_courses) / actual_sks
    else:
        pred_ips = 0.0
    pred_ips = round(pred_ips, 2)

    # Predict new IPK
    total_sks = cumulative_sks_so_far + actual_sks
    pred_ipk = (cumulative_sks_so_far * current_ipk + pred_ips * actual_sks) / total_sks if total_sks > 0 else pred_ips
    pred_ipk = round(max(0.0, min(4.0, pred_ipk)), 2)

    return {
        "sks": actual_sks,
        "prediksi_ips": pred_ips,
        "prediksi_ipk": pred_ipk,
        "matkul_count": len(selected_courses),
        "matkul": [
            {
                "kode": c["kode"],
                "nama": c["nama"],
                "sks": c["sks"],
                "wajib": c["wajib"],
                "prediksi_nilai_huruf": c["prediksi_nilai_huruf"],
                "prediksi_nilai_angka": c["prediksi_nilai_angka"],
                "confidence": c["confidence"],
            }
            for c in selected_courses
        ],
    }


def predict_student(student: dict) -> dict:
    """Generate full prediction for a student."""
    nim = student["nim"]
    # Gunakan prodi_key langsung dari data student, bukan parsing NIM
    prodi_key = student.get("prodi_key") or get_prodi_key(nim)
    riwayat = student["riwayat_semester"]
    semester_aktif = student.get("semester_aktif", 3)
    # Semester aktif = semester yang sedang berjalan, prediksi untuk semester ini
    semester_target = semester_aktif

    # Hanya ambil riwayat semester yang sudah selesai (sebelum semester aktif)
    riwayat_selesai = [s for s in riwayat if s["semester"] < semester_aktif]

    # Extract IPS history dari semester yang sudah selesai
    ips_by_sem = {entry["semester"]: entry["ips"] for entry in riwayat_selesai}
    sks_by_sem = {entry["semester"]: entry["sks"] for entry in riwayat_selesai}

    ips_list = [ips_by_sem.get(s, 0.0) for s in sorted(ips_by_sem.keys())]

    if len(ips_list) >= 3:
        ips1, ips2, ips3 = ips_list[-3], ips_list[-2], ips_list[-1]
        weighted_avg = ips3 * 0.5 + ips2 * 0.3 + ips1 * 0.2
        trend = ips3 - ips2
    elif len(ips_list) == 2:
        ips2, ips3 = ips_list[-2], ips_list[-1]
        weighted_avg = ips3 * 0.6 + ips2 * 0.4
        trend = ips3 - ips2
    elif len(ips_list) == 1:
        weighted_avg = ips_list[0]
        trend = 0.0
    else:
        weighted_avg = 2.5
        trend = 0.0

    # Predicted IPS for target semester (dari weighted avg riwayat + trend)
    # Ini hanya dipakai sebagai fallback; nilai final diambil dari rec_scenario
    predicted_ips_fallback = weighted_avg + (trend * 0.15)
    predicted_ips_fallback = max(0.0, min(4.0, round(predicted_ips_fallback, 2)))

    # Cumulative SKS dari semester yang sudah selesai (sebelum semester aktif)
    cumulative_sks = sum(sks_by_sem.get(s, 0) for s in range(1, semester_aktif))

    current_ipk = student["ipk_kumulatif"]

    # SKS recommendation based on current IPK using the new function
    rekomendasi_sks = get_max_sks_by_ipk(current_ipk, semester_aktif)

    # Overall confidence based on data quality
    if len(ips_list) >= 2:
        trend_stable = abs(ips_list[-1] - ips_list[-2]) < 0.5
    else:
        trend_stable = True
    overall_confidence = 70.0 + (20.0 if trend_stable else 5.0)
    if len(ips_list) >= 3:
        overall_confidence += 5.0
    overall_confidence = round(max(60.0, min(95.0, overall_confidence)), 1)

    # Trend label
    if trend > 0.1:
        trend_label = "meningkat"
    elif trend < -0.1:
        trend_label = "menurun"
    else:
        trend_label = "stabil"

    # Get all courses for target semester
    target_semester_courses = CURRICULUM[prodi_key]["semesters"].get(semester_target, [])
    
    # Get completed courses for prerequisite validation
    completed_courses = get_completed_courses(riwayat)
    
    # Get cohort average
    cohort_avg = get_cohort_average(prodi_key, student.get("angkatan", 2024))

    # Predict grade for each course in target semester
    all_courses_predicted = []
    for course in target_semester_courses:
        course_code = course["kode"]
        
        # Validate prerequisites
        prereq_valid, missing_prereqs = validate_prerequisites(course_code, completed_courses)
        
        # Get related courses average
        related_avg = get_related_courses_avg(course_code, riwayat, prodi_key)
        if related_avg == 0.0:
            related_avg = current_ipk  # Fallback to IPK if no related courses
        
        pred = predict_course_grade(
            kode=course_code,
            wajib=course.get("wajib", False),
            historical_ipk=predicted_ips_fallback,
            related_courses_avg=related_avg,
            cohort_avg=cohort_avg,
            trend=trend,
        )
        
        course_data = {
            "kode": course["kode"],
            "nama": course["nama"],
            "sks": course["sks"],
            "wajib": course.get("wajib", False),
            "prediksi_nilai_huruf": pred["prediksi_nilai_huruf"],
            "prediksi_nilai_angka": pred["prediksi_nilai_angka"],
            "confidence": pred["confidence"],
            "prasyarat_terpenuhi": prereq_valid,
        }
        
        if not prereq_valid:
            course_data["prasyarat_belum_lulus"] = missing_prereqs
        
        all_courses_predicted.append(course_data)

    # Filter courses: only include those with prerequisites met
    eligible_courses = [c for c in all_courses_predicted if c.get("prasyarat_terpenuhi", True)]
    ineligible_courses = [c for c in all_courses_predicted if not c.get("prasyarat_terpenuhi", True)]
    
    # Sort eligible: wajib first, then pilihan by predicted grade desc
    wajib_pred = sorted(
        [c for c in eligible_courses if c["wajib"]],
        key=lambda c: c["prediksi_nilai_angka"],
        reverse=True,
    )
    pilihan_pred = sorted(
        [c for c in eligible_courses if not c["wajib"]],
        key=lambda c: c["prediksi_nilai_angka"],
        reverse=True,
    )
    all_sorted = wajib_pred + pilihan_pred

    # Build SKS scenarios (18, 20, 22, 24) - realistic range
    sks_scenarios = []
    for target_sks in [18, 20, 22, 24]:
        # Only build scenario if it's within allowed limit
        max_allowed = get_max_sks_by_ipk(current_ipk, semester_aktif)
        if target_sks <= max_allowed:
            scenario = build_sks_scenario(
                nim=nim,
                prodi_key=prodi_key,
                semester_target=semester_target,
                all_courses_predicted=all_sorted,
                target_sks=target_sks,
                current_ipk=current_ipk,
                cumulative_sks_so_far=cumulative_sks,
            )
            sks_scenarios.append(scenario)

    # Default recommendation: courses for the recommended SKS scenario
    rec_scenario = next(
        (s for s in sks_scenarios if s["sks"] == rekomendasi_sks),
        sks_scenarios[-1]
    )
    matakuliah_direkomendasikan = rec_scenario["matkul"]

    # Gunakan IPS dari scenario rekomendasi sebagai prediksi IPS utama
    rec_sks = rec_scenario["sks"]
    predicted_ips = rec_scenario["prediksi_ips"]

    # Predicted IPK: gabungkan IPK lama dengan IPS prediksi semester ini
    predicted_ipk = (cumulative_sks * current_ipk + predicted_ips * rec_sks) / (
        cumulative_sks + rec_sks
    ) if (cumulative_sks + rec_sks) > 0 else predicted_ips
    predicted_ipk = round(max(0.0, min(4.0, predicted_ipk)), 2)

    # Academic notes
    catatan = generate_catatan(current_ipk, trend_label, predicted_ips, predicted_ipk, semester_target)

    return {
        "semester_target": semester_target,
        "prediksi_ips": predicted_ips,
        "prediksi_ipk_baru": predicted_ipk,
        "rekomendasi_sks": rekomendasi_sks,
        "max_sks_allowed": get_max_sks_by_ipk(current_ipk, semester_aktif),
        "confidence": overall_confidence,
        "trend": trend_label,
        "all_semester_courses": all_sorted,
        "matakuliah_direkomendasikan": matakuliah_direkomendasikan,
        "matakuliah_prasyarat_belum_terpenuhi": ineligible_courses,
        "sks_scenarios": sks_scenarios,
        "catatan_akademik": catatan,
        "generated_at": str(date.today()),
    }


def generate_catatan(ipk: float, trend: str, pred_ips: float, pred_ipk: float, semester_target: int) -> str:
    """Generate academic notes based on performance."""
    lines = []

    if ipk >= 3.5:
        lines.append(
            f"Mahasiswa menunjukkan performa akademik yang sangat baik dengan IPK kumulatif {ipk:.2f}."
        )
    elif ipk >= 3.0:
        lines.append(
            f"Mahasiswa memiliki performa akademik yang baik dengan IPK kumulatif {ipk:.2f}."
        )
    elif ipk >= 2.5:
        lines.append(
            f"Mahasiswa memiliki performa akademik yang cukup dengan IPK kumulatif {ipk:.2f}. Diperlukan peningkatan."
        )
    else:
        lines.append(
            f"Mahasiswa perlu perhatian khusus dengan IPK kumulatif {ipk:.2f}. Sangat disarankan konsultasi dengan dosen pembimbing."
        )

    if trend == "meningkat":
        lines.append(
            "Tren akademik menunjukkan peningkatan yang positif dari semester ke semester."
        )
    elif trend == "menurun":
        lines.append(
            "Tren akademik menunjukkan penurunan. Perlu evaluasi faktor-faktor yang mempengaruhi prestasi."
        )
    else:
        lines.append("Tren akademik relatif stabil.")

    lines.append(
        f"Prediksi IPS semester {semester_target}: {pred_ips:.2f}, dengan prediksi IPK baru: {pred_ipk:.2f}."
    )
    # Penjelasan jujur jika IPK tidak naik signifikan
    if pred_ipk <= ipk:
        lines.append(
            "Catatan: IPK kumulatif sulit naik signifikan di semester lanjut karena bobot SKS lama lebih besar. "
            "Fokus pertahankan IPS tinggi setiap semester untuk menjaga IPK."
        )
    else:
        lines.append(
            f"Dengan IPS prediksi {pred_ips:.2f}, IPK diperkirakan dapat meningkat menjadi {pred_ipk:.2f}."
        )
    lines.append(
        "Untuk klarifikasi atau penyempurnaan lebih lanjut, silakan diskusi."
    )

    return " ".join(lines)
      
