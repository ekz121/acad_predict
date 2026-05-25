# ═══════════════════════════════════════════════════════════════════════════
# FILE: backend/utils/predictor.py
# DEVELOPER: Anak 4 (Backend - Predictor & IPK Target)
# DESKRIPSI: Modul prediksi performa akademik mahasiswa
# ═══════════════════════════════════════════════════════════════════════════

# ─── BAGIAN 1: IMPORT STATEMENTS ──────────────────────────────────────────

from datetime import date

from .curriculum import (
    CURRICULUM,
    get_prodi_key,
    get_max_sks_by_ipk,
    validate_prerequisites,
    get_completed_courses 
)

# ─── BAGIAN 2: HELPER FUNCTIONS ───────────────────────────────────────────


def get_related_courses_avg(
    kode: str,
    riwayat_semester: list,
    prodi_key: str
) -> float:
    """
    Hitung rata-rata nilai seluruh mata kuliah
    """

    all_grades = []

    for semester in riwayat_semester:

        nilai_matkul = semester.get(
            "nilai_matkul",
            []
        )

        for nilai in nilai_matkul:

            nilai_angka = nilai.get(
                "nilai_angka"
            )

            if nilai_angka is not None:
                all_grades.append(nilai_angka)

    if not all_grades:
        return 0.0

    return round(
        sum(all_grades) / len(all_grades),
        2
    )


def get_cohort_average(
    prodi_key: str,
    angkatan: int
) -> float:
    """
    Rata-rata IPK cohort berdasarkan prodi
    """

    cohort_defaults = {
        "TI": 3.15,
        "AK": 3.20,
        "TM": 3.10,
        "AP": 3.18
    }

    return cohort_defaults.get(
        prodi_key,
        3.15
    )


def predict_course_grade(
    kode: str,
    wajib: bool,
    historical_ipk: float,
    related_courses_avg: float,
    cohort_avg: float,
    trend: float
) -> dict:
    """
    Prediksi nilai mata kuliah
    """

    # ─── BASE PREDICTION ────────────────────────────────

    if related_courses_avg > 0:

        base = (
            (historical_ipk * 0.6) +
            (related_courses_avg * 0.4)
        )

    else:
        base = historical_ipk

    # ─── COHORT ADJUSTMENT ─────────────────────────────

    if historical_ipk < cohort_avg:

        base = (
            (base * 0.85) +
            (cohort_avg * 0.15)
        )

    # ─── TREND ADJUSTMENT ──────────────────────────────

    trend_adjustment = max(
        -0.5,
        min(0.5, trend * 0.2)
    )

    raw = base + trend_adjustment

    raw = max(
        0.0,
        min(4.0, raw)
    )

    # ─── GRADE CONVERSION ──────────────────────────────

    grade_points = [
        4.0,
        3.5,
        3.0,
        2.5,
        2.0,
        1.0,
        0.0
    ]

    grade_letters = [
        "A",
        "AB",
        "B",
        "BC",
        "C",
        "D",
        "E"
    ]

    closest = min(
        grade_points,
        key=lambda x: abs(x - raw)
    )

    grade_index = grade_points.index(
        closest
    )

    prediksi_huruf = grade_letters[
        grade_index
    ]

    # ─── CONFIDENCE ────────────────────────────────────

    confidence = 70

    if related_courses_avg > 0:
        confidence += 10

    if abs(trend) < 0.3:
        confidence += 10

    if historical_ipk >= 3.0:
        confidence += 5

    confidence = min(confidence, 95)

    return {
        "kode": kode,
        "prediksi_nilai_angka": round(
            closest,
            2
        ),
        "prediksi_nilai_huruf": prediksi_huruf,
        "confidence": confidence
    }


# ─── BAGIAN 3: SKS SCENARIO BUILDER ──────────────────────────────────────


def build_sks_scenario(
    nim: str,
    prodi_key: str,
    semester_target: int,
    all_courses_predicted: list,
    target_sks: int,
    current_ipk: float,
    cumulative_sks_so_far: int
) -> dict:
    """
    Build skenario pengambilan SKS
    """

    wajib_courses = [
        c for c in all_courses_predicted
        if c["wajib"]
    ]

    pilihan_courses = [
        c for c in all_courses_predicted
        if not c["wajib"]
    ]

    selected = list(wajib_courses)

    current_sks = sum(
        c["sks"]
        for c in selected
    )

    # ─── TAMBAH MATA KULIAH PILIHAN ────────────────────

    if current_sks < target_sks:

        pilihan_sorted = sorted(
            pilihan_courses,
            key=lambda x:
                x["prediksi_nilai_angka"],
            reverse=True
        )

        while (
            current_sks < target_sks and
            pilihan_sorted
        ):

            needed = (
                target_sks -
                current_sks
            )

            best_fit = None

            # Exact match
            for course in pilihan_sorted:

                if course["sks"] == needed:
                    best_fit = course
                    break

            # Cari yang <= needed
            if best_fit is None:

                valid_under = [
                    c for c in pilihan_sorted
                    if c["sks"] <= needed
                ]

                if valid_under:
                    best_fit = valid_under[0]

            # Jika tetap tidak ada
            if best_fit is None:
                best_fit = pilihan_sorted[0]

            selected.append(best_fit)

            current_sks += best_fit["sks"]

            pilihan_sorted.remove(best_fit)

    # ─── HITUNG IPS ────────────────────────────────────

    actual_sks = sum(
        c["sks"]
        for c in selected
    )

    if actual_sks > 0:

        pred_ips = (
            sum(
                c["prediksi_nilai_angka"] * c["sks"]
                for c in selected
            ) / actual_sks
        )

    else:
        pred_ips = 0.0

    pred_ips = round(pred_ips, 2)

    # ─── HITUNG IPK ────────────────────────────────────

    total_sks = (
        cumulative_sks_so_far +
        actual_sks
    )

    if total_sks > 0:

        pred_ipk = (
            (
                cumulative_sks_so_far *
                current_ipk
            ) +
            (
                pred_ips *
                actual_sks
            )
        ) / total_sks

    else:
        pred_ipk = current_ipk

    pred_ipk = round(
        max(
            0.0,
            min(4.0, pred_ipk)
        ),
        2
    )

    return {
        "sks": actual_sks,
        "prediksi_ips": pred_ips,
        "prediksi_ipk": pred_ipk,
        "matkul_count": len(selected),
        "matkul": selected
    }


# ─── BAGIAN 4: MAIN PREDICTION FUNCTION ──────────────────────────────────


def predict_student(student: dict) -> dict:
    """
    Generate prediksi lengkap mahasiswa
    """

    nim = student.get("nim")

    prodi_key = get_prodi_key(
        student.get("prodi")
    )

    riwayat = student.get(
        "riwayat_semester",
        []
    )

    semester_aktif = student.get(
        "semester_aktif",
        1
    )

    semester_target = semester_aktif

    current_ipk = student.get(
        "ipk_kumulatif",
        0.0
    )

    # ─── RIWAYAT SELESAI ───────────────────────────────

    riwayat_selesai = [
        s for s in riwayat
        if s["semester"] < semester_aktif
    ]

    ips_list = [
        s.get("ips", 0.0)
        for s in riwayat_selesai
    ]

    # ─── WEIGHTED AVERAGE & TREND ──────────────────────

    trend = 0.0

    if len(ips_list) >= 3:

        ips1, ips2, ips3 = ips_list[-3:]

        weighted_avg = (
            (ips3 * 0.5) +
            (ips2 * 0.3) +
            (ips1 * 0.2)
        )

        trend = ips3 - ips2

    elif len(ips_list) == 2:

        ips2, ips3 = ips_list[-2:]

        weighted_avg = (
            (ips3 * 0.6) +
            (ips2 * 0.4)
        )

        trend = ips3 - ips2

    elif len(ips_list) == 1:

        weighted_avg = ips_list[0]

    else:

        weighted_avg = 2.5

    predicted_ips_fallback = (
        weighted_avg +
        (trend * 0.15)
    )

    predicted_ips_fallback = round(
        max(
            0.0,
            min(
                4.0,
                predicted_ips_fallback
            )
        ),
        2
    )

    # ─── CUMULATIVE SKS ────────────────────────────────

    cumulative_sks = sum(
        s.get("sks", 0)
        for s in riwayat_selesai
    )

    rekomendasi_sks = get_max_sks_by_ipk(
        current_ipk,
        semester_aktif
    )

    # ─── CONFIDENCE ────────────────────────────────────

    confidence = 70

    if len(ips_list) >= 2:

        if abs(
            ips_list[-1] -
            ips_list[-2]
        ) < 0.5:

            confidence += 20

    if len(ips_list) >= 3:
        confidence += 5

    confidence = max(
        60,
        min(95, confidence)
    )

    # ─── TREND LABEL ───────────────────────────────────

    if trend > 0.1:
        trend_label = "meningkat"

    elif trend < -0.1:
        trend_label = "menurun"

    else:
        trend_label = "stabil"

    # ─── TARGET COURSES ────────────────────────────────

    target_semester_courses = (
        CURRICULUM[prodi_key]
        ["semesters"]
        .get(semester_target, [])
    )

    completed_courses = get_completed_courses(
        riwayat
    )

    cohort_avg = get_cohort_average(
        prodi_key,
        student.get("angkatan", 2024)
    )

    all_courses_predicted = []

    # ─── PREDIKSI TIAP MATA KULIAH ─────────────────────

    for course in target_semester_courses:

        kode = course.get("kode")
        nama = course.get("nama")
        sks = course.get("sks")

        wajib = course.get(
            "wajib",
            True
        )

        prasyarat_ok = validate_prerequisites(
            course,
            completed_courses
        )

        related_avg = get_related_courses_avg(
            kode,
            riwayat,
            prodi_key
        )

        prediction = predict_course_grade(
            kode=kode,
            wajib=wajib,
            historical_ipk=current_ipk,
            related_courses_avg=related_avg,
            cohort_avg=cohort_avg,
            trend=trend
        )

        course_data = {
            "kode": kode,
            "nama": nama,
            "sks": sks,
            "wajib": wajib,
            "prasyarat_terpenuhi": prasyarat_ok,
            "prediksi_nilai_angka":
                prediction[
                    "prediksi_nilai_angka"
                ],
            "prediksi_nilai_huruf":
                prediction[
                    "prediksi_nilai_huruf"
                ],
            "confidence":
                prediction["confidence"]
        }

        all_courses_predicted.append(
            course_data
        )

    eligible_courses = [
        c for c in all_courses_predicted
        if c["prasyarat_terpenuhi"]
    ]

    ineligible_courses = [
        c for c in all_courses_predicted
        if not c["prasyarat_terpenuhi"]
    ]

    # ─── SKS SCENARIOS ─────────────────────────────────

    sks_scenarios = []

    for target_sks in [18, 20, 22, 24]:

        max_allowed = get_max_sks_by_ipk(
            current_ipk,
            semester_aktif
        )

        if target_sks <= max_allowed:

            scenario = build_sks_scenario(
                nim=nim,
                prodi_key=prodi_key,
                semester_target=semester_target,
                all_courses_predicted=eligible_courses,
                target_sks=target_sks,
                current_ipk=current_ipk,
                cumulative_sks_so_far=cumulative_sks
            )

            sks_scenarios.append(
                scenario
            )

    # ─── RECOMMENDED SCENARIO ──────────────────────────

    rec_scenario = None

    for sc in sks_scenarios:

        if sc["sks"] == rekomendasi_sks:
            rec_scenario = sc
            break

    if rec_scenario is None and sks_scenarios:
        rec_scenario = sks_scenarios[-1]

    if rec_scenario:

        matakuliah_direkomendasikan = (
            rec_scenario["matkul"]
        )

        rec_sks = rec_scenario["sks"]

        predicted_ips = (
            rec_scenario["prediksi_ips"]
        )

    else:

        matakuliah_direkomendasikan = []

        rec_sks = 0

        predicted_ips = (
            predicted_ips_fallback
        )

    # ─── PREDICTED IPK ─────────────────────────────────

    total_future_sks = (
        cumulative_sks +
        rec_sks
    )

    if total_future_sks > 0:

        predicted_ipk = (
            (
                cumulative_sks *
                current_ipk
            ) +
            (
                predicted_ips *
                rec_sks
            )
        ) / total_future_sks

    else:
        predicted_ipk = current_ipk

    predicted_ipk = round(
        max(
            0.0,
            min(4.0, predicted_ipk)
        ),
        2
    )

    # ─── CATATAN AKADEMIK ──────────────────────────────

    catatan = generate_catatan(
        current_ipk,
        trend_label,
        predicted_ips,
        predicted_ipk,
        semester_target
    )

    return {
        "nim": nim,
        "tanggal_prediksi": str(date.today()),
        "semester_target": semester_target,
        "trend": trend_label,
        "confidence": confidence,
        "current_ipk": current_ipk,
        "predicted_ips": predicted_ips,
        "predicted_ipk": predicted_ipk,
        "recommended_sks": rec_sks,
        "matakuliah_direkomendasikan":
            matakuliah_direkomendasikan,
        "eligible_courses":
            eligible_courses,
        "ineligible_courses":
            ineligible_courses,
        "sks_scenarios":
            sks_scenarios,
        "catatan_akademik":
            catatan
    }


# ─── BAGIAN 5: CATATAN AKADEMIK GENERATOR ────────────────────────────────


def generate_catatan(
    ipk,
    trend,
    pred_ips,
    pred_ipk,
    semester_target
) -> str:
    """
    Generate catatan akademik otomatis
    """

    lines = []

    if ipk >= 3.5:

        lines.append(
            "Mahasiswa menunjukkan performa "
            "akademik yang sangat baik."
        )

    elif ipk >= 3.0:

        lines.append(
            "Mahasiswa memiliki performa "
            "akademik yang baik."
        )

    elif ipk >= 2.5:

        lines.append(
            "Mahasiswa memiliki performa "
            "akademik yang cukup. "
            "Diperlukan peningkatan."
        )

    else:

        lines.append(
            "Mahasiswa perlu perhatian khusus. "
            "Sangat disarankan konsultasi akademik."
        )

    if trend == "meningkat":

        lines.append(
            "Tren akademik menunjukkan "
            "peningkatan yang positif."
        )

    elif trend == "menurun":

        lines.append(
            "Tren akademik menunjukkan "
            "penurunan."
        )

    else:

        lines.append(
            "Tren akademik relatif stabil."
        )

    lines.append(
        f"Prediksi IPS semester "
        f"{semester_target}: "
        f"{pred_ips:.2f}, "
        f"dengan prediksi IPK baru: "
        f"{pred_ipk:.2f}."
    )

    if pred_ipk <= ipk:

        lines.append(
            "IPK kumulatif sulit naik "
            "secara signifikan pada "
            "semester lanjut."
        )

    else:

        lines.append(
            "IPK diperkirakan meningkat "
            "jika performa tetap konsisten."
        )

    lines.append(
        "Silakan lakukan evaluasi rutin "
        "dan konsultasi akademik."
    )

    return " ".join(lines)
