# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 1: IMPORT
# ═══════════════════════════════════════════════════════════════════════════
from datetime import date

from .curriculum import (
    CURRICULUM,
    get_prodi_key,
    get_wajib_courses,
    get_pilihan_courses,
    get_max_sks_by_ipk,
    validate_prerequisites,
    get_completed_courses
)

# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 2: HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def get_related_courses_avg(kode: str, riwayat_semester: list, prodi_key: str) -> float:
    all_grades = []

    for semester in riwayat_semester:
        nilai_matkul = semester.get("nilai_matkul", [])
        for nilai in nilai_matkul:
            nilai_angka = nilai.get("nilai_angka")
            if nilai_angka is not None:
                all_grades.append(nilai_angka)

    return sum(all_grades) / len(all_grades) if all_grades else 0.0


def get_cohort_average(prodi_key: str, angkatan: int) -> float:
    cohort_defaults = {
        "TI": 3.15,
        "AK": 3.20,
        "TM": 3.10,
        "AP": 3.18
    }
    return cohort_defaults.get(prodi_key, 3.15)


def predict_course_grade(kode, wajib, historical_ipk, related_courses_avg, cohort_avg, trend):
    # Base prediction
    if related_courses_avg > 0:
        base = (historical_ipk * 0.6) + (related_courses_avg * 0.4)
    else:
        base = historical_ipk

    # Adjust dengan cohort
    if historical_ipk < cohort_avg:
        base = base * 0.85 + cohort_avg * 0.15

    # Trend adjustment
    trend_adjustment = max(-0.5, min(0.5, trend * 0.2))
    raw = base + trend_adjustment
    raw = max(0.0, min(4.0, raw))

    # Grade mapping
    grade_points = [4.0, 3.5, 3.0, 2.5, 2.0, 1.0, 0.0]
    grade_letters = ["A", "AB", "B", "BC", "C", "D", "E"]

    closest = min(grade_points, key=lambda x: abs(x - raw))
    letter = grade_letters[grade_points.index(closest)]

    # Confidence
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
        "prediksi_nilai_angka": round(closest, 2),
        "prediksi_nilai_huruf": letter,
        "confidence": confidence
    }


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 3: SKS SCENARIO BUILDER
# ═══════════════════════════════════════════════════════════════════════════

def build_sks_scenario(nim, prodi_key, semester_target, all_courses_predicted,
                       target_sks, current_ipk, cumulative_sks_so_far):

    wajib_courses = [c for c in all_courses_predicted if c["wajib"]]
    pilihan_courses = [c for c in all_courses_predicted if not c["wajib"]]

    selected = list(wajib_courses)
    current_sks = sum(c["sks"] for c in selected)

    if current_sks < target_sks:
        pilihan_sorted = sorted(
            pilihan_courses,
            key=lambda c: c["prediksi_nilai_angka"],
            reverse=True
        )

        while current_sks < target_sks and pilihan_sorted:
            needed = target_sks - current_sks

            exact = next((c for c in pilihan_sorted if c["sks"] == needed), None)
            if exact:
                chosen = exact
            else:
                under = [c for c in pilihan_sorted if c["sks"] <= needed]
                if under:
                    chosen = under[0]
                else:
                    chosen = pilihan_sorted[0]

            selected.append(chosen)
            pilihan_sorted.remove(chosen)
            current_sks += chosen["sks"]

    actual_sks = sum(c["sks"] for c in selected)

    pred_ips = sum(c["prediksi_nilai_angka"] * c["sks"] for c in selected) / actual_sks
    pred_ips = round(pred_ips, 2)

    total_sks = cumulative_sks_so_far + actual_sks
    pred_ipk = (
        (cumulative_sks_so_far * current_ipk) +
        (pred_ips * actual_sks)
    ) / total_sks

    pred_ipk = round(max(0.0, min(4.0, pred_ipk)), 2)

    return {
        "sks": actual_sks,
        "prediksi_ips": pred_ips,
        "prediksi_ipk": pred_ipk,
        "matkul_count": len(selected),
        "matkul": selected
    }


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 4: MAIN PREDICTION FUNCTION
# ═══════════════════════════════════════════════════════════════════════════

def predict_student(student: dict) -> dict:
    nim = student["nim"]
    prodi_key = get_prodi_key(student["prodi"])
    riwayat = student.get("riwayat_semester", [])
    semester_aktif = student["semester_aktif"]
    semester_target = semester_aktif

    riwayat_selesai = [s for s in riwayat if s["semester"] < semester_aktif]

    ips_by_sem = {s["semester"]: s["ips"] for s in riwayat_selesai}
    sks_by_sem = {s["semester"]: s["sks"] for s in riwayat_selesai}

    ips_list = [ips_by_sem[s] for s in sorted(ips_by_sem.keys())]

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

    predicted_ips_fallback = round(max(0, min(4, weighted_avg + trend * 0.15)), 2)

    cumulative_sks = sum(sks_by_sem.values())

    current_ipk = student["ipk_kumulatif"]
    rekomendasi_sks = get_max_sks_by_ipk(current_ipk, semester_aktif)

    confidence = 70
    if len(ips_list) >= 2 and abs(ips_list[-1] - ips_list[-2]) < 0.5:
        confidence += 20
    if len(ips_list) >= 3:
        confidence += 5

    confidence = round(max(60, min(95, confidence)), 1)

    if trend > 0.1:
        trend_label = "meningkat"
    elif trend < -0.1:
        trend_label = "menurun"
    else:
        trend_label = "stabil"

    target_courses = CURRICULUM[prodi_key]["semesters"].get(semester_target, [])

    completed_courses = get_completed_courses(riwayat)
    cohort_avg = get_cohort_average(prodi_key, student.get("angkatan", 2024))

    all_courses_predicted = []

    for course in target_courses:
        kode = course["kode"]
        wajib = course.get("wajib", True)

        prasyarat_ok = validate_prerequisites(kode, completed_courses, prodi_key)

        related_avg = get_related_courses_avg(kode, riwayat, prodi_key)

        pred = predict_course_grade(
            kode, wajib, current_ipk, related_avg, cohort_avg, trend
        )

        course_data = {
            **course,
            **pred,
            "prasyarat_terpenuhi": prasyarat_ok
        }

        all_courses_predicted.append(course_data)

    eligible = [c for c in all_courses_predicted if c["prasyarat_terpenuhi"]]
    ineligible = [c for c in all_courses_predicted if not c["prasyarat_terpenuhi"]]

    wajib_pred = sorted(
        [c for c in eligible if c["wajib"]],
        key=lambda c: c["prediksi_nilai_angka"],
        reverse=True
    )

    pilihan_pred = sorted(
        [c for c in eligible if not c["wajib"]],
        key=lambda c: c["prediksi_nilai_angka"],
        reverse=True
    )

    all_sorted = wajib_pred + pilihan_pred

    sks_scenarios = []
    for target_sks in [18, 20, 22, 24]:
        max_allowed = get_max_sks_by_ipk(current_ipk, semester_aktif)
        if target_sks <= max_allowed:
            scenario = build_sks_scenario(
                nim, prodi_key, semester_target,
                all_sorted, target_sks,
                current_ipk, cumulative_sks
            )
            sks_scenarios.append(scenario)

    rec_scenario = next(
        (s for s in sks_scenarios if s["sks"] == rekomendasi_sks),
        sks_scenarios[-1] if sks_scenarios else None
    )

    if rec_scenario:
        matakuliah_direkomendasikan = rec_scenario["matkul"]
        rec_sks = rec_scenario["sks"]
        predicted_ips = rec_scenario["prediksi_ips"]
    else:
        matakuliah_direkomendasikan = []
        rec_sks = 0
        predicted_ips = predicted_ips_fallback

    total_sks = cumulative_sks + rec_sks if rec_sks else cumulative_sks
    predicted_ipk = (
        (cumulative_sks * current_ipk + predicted_ips * rec_sks) / total_sks
        if total_sks else current_ipk
    )

    predicted_ipk = round(max(0, min(4, predicted_ipk)), 2)

    catatan = generate_catatan(
        current_ipk, trend_label,
        predicted_ips, predicted_ipk,
        semester_target
    )

    return {
        "nim": nim,
        "semester_target": semester_target,
        "predicted_ips": predicted_ips,
        "predicted_ipk": predicted_ipk,
        "confidence": confidence,
        "trend": trend_label,
        "recommended_sks": rec_sks,
        "mata_kuliah": matakuliah_direkomendasikan,
        "sks_scenarios": sks_scenarios,
        "ineligible_courses": ineligible,
        "catatan": catatan,
        "generated_at": date.today().isoformat()
    }


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 5: CATATAN AKADEMIK
# ═══════════════════════════════════════════════════════════════════════════

def generate_catatan(ipk, trend, pred_ips, pred_ipk, semester_target):
    lines = []

    if ipk >= 3.5:
        lines.append("Mahasiswa menunjukkan performa akademik yang sangat baik.")
    elif ipk >= 3.0:
        lines.append("Mahasiswa memiliki performa akademik yang baik.")
    elif ipk >= 2.5:
        lines.append("Mahasiswa memiliki performa akademik yang cukup. Diperlukan peningkatan.")
    else:
        lines.append("Mahasiswa perlu perhatian khusus dan sangat disarankan konsultasi akademik.")

    if trend == "meningkat":
        lines.append("Tren akademik menunjukkan peningkatan yang positif.")
    elif trend == "menurun":
        lines.append("Tren akademik menunjukkan penurunan. Perlu evaluasi.")
    else:
        lines.append("Tren akademik relatif stabil.")

    lines.append(
        f"Prediksi IPS semester {semester_target}: {pred_ips:.2f}, "
        f"dengan prediksi IPK baru: {pred_ipk:.2f}."
    )

    if pred_ipk <= ipk:
        lines.append("Catatan: IPK kumulatif sulit naik signifikan di semester lanjut.")
    else:
        lines.append(f"Dengan IPS {pred_ips:.2f}, IPK diperkirakan dapat meningkat.")

    lines.append("Untuk klarifikasi atau penyempurnaan lebih lanjut, silakan diskusi.")

    return " ".join(lines)
