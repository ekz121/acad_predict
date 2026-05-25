# ═══════════════════════════════════════════════════════════════════════════
# FILE: backend/utils/ipk_target.py
# DEVELOPER: Anak 4 (Backend - Predictor & IPK Target)
# DESKRIPSI: Analisis Target IPK dengan panduan personal
# ═══════════════════════════════════════════════════════════════════════════

# ─── BAGIAN 1: IMPORT & CONSTANTS ─────────────────────────────────────────

from math import ceil

TOTAL_SEMESTER = 6
SKS_PER_SEMESTER = 22


# ─── BAGIAN 2: HELPER FUNCTIONS ───────────────────────────────────────────


def _ips_minimum(
    target_ipk,
    current_ipk,
    sks_lulus,
    sisa_semester
):
    """
    Hitung IPS minimum yang harus dicapai tiap semester
    """

    sks_sisa = sisa_semester * SKS_PER_SEMESTER

    total_sks = sks_lulus + sks_sisa

    if sks_sisa > 0:
        ips_min = (
            (target_ipk * total_sks) -
            (current_ipk * sks_lulus)
        ) / sks_sisa
    else:
        ips_min = 0.0

    ips_min = max(0.0, min(4.0, ips_min))

    return round(ips_min, 2)


def _proyeksi_ipk(
    current_ipk,
    sks_lulus,
    ips_per_sem,
    sisa_semester
):
    """
    Proyeksi IPK per semester
    """

    rows = []

    ipk = current_ipk
    sks = sks_lulus

    for i in range(1, sisa_semester + 1):

        sks += SKS_PER_SEMESTER

        ipk = round(
            (
                (
                    ipk * (sks - SKS_PER_SEMESTER)
                ) +
                (
                    ips_per_sem * SKS_PER_SEMESTER
                )
            ) / sks,
            2
        )

        rows.append({
            "semester_ke": i,
            "ipk_proyeksi": ipk
        })

    return rows


def _validasi_target(
    target_ipk,
    current_ipk,
    pred_ipk,
    sisa_semester
):
    """
    Validasi target IPK
    """

    if target_ipk > 4.0:

        return {
            "status": "tidak_valid",
            "label": "Tidak Valid",
            "pesan": "Target IPK tidak boleh melebihi 4.00."
        }

    ips_min = _ips_minimum(
        target_ipk,
        current_ipk,
        0,
        sisa_semester
    )

    if ips_min > 4.0:

        return {
            "status": "tidak_mungkin",
            "label": "Tidak Mungkin",
            "pesan": (
                f"Target IPK {target_ipk:.2f} "
                "tidak dapat dicapai dengan sisa semester yang ada."
            )
        }

    gap = target_ipk - current_ipk

    if gap <= 0.05:

        return {
            "status": "realistis",
            "label": "Realistis ✓",
            "pesan": (
                "Target sudah sesuai dengan kemampuan akademik saat ini."
            )
        }

    if ips_min <= 3.5 and sisa_semester >= 2:

        return {
            "status": "realistis",
            "label": "Realistis ✓",
            "pesan": (
                "Target dapat dicapai dengan konsistensi belajar yang baik."
            )
        }

    if ips_min <= 4.0 and sisa_semester >= 1:

        return {
            "status": "ambisius",
            "label": "Ambisius ⚡",
            "pesan": (
                "Target cukup ambisius dan membutuhkan usaha ekstra."
            )
        }

    return {
        "status": "tidak_mungkin",
        "label": "Tidak Mungkin ✗",
        "pesan": (
            "Target terlalu tinggi untuk dicapai "
            "dengan kondisi akademik saat ini."
        )
    }


# ─── BAGIAN 3: PANDUAN PERSONAL GENERATOR ────────────────────────────────


def _panduan_personal(
    target_ipk,
    current_ipk,
    validasi_status,
    kebiasaan,
    gaya,
    matkul_tersulit,
    sisa_semester,
    ips_min,
    pred_ipk
):
    """
    Generate panduan personal mahasiswa
    """

    nama_gaya = {
        "visual": "visual (diagram/mind map)",
        "membaca": "membaca & mencatat",
        "diskusi": "diskusi kelompok",
        "praktek": "praktek langsung"
    }

    nama_kebiasaan = {
        "rutin": "rutin setiap hari",
        "kadang": "kadang-kadang",
        "jarang": "jarang belajar"
    }

    lines = []

    # PEMBUKA
    if validasi_status == "realistis":

        lines.append(
            f"🎯 Target IPK {target_ipk:.2f} sangat realistis untukmu! "
            "Dengan strategi yang tepat, target ini dapat dicapai."
        )

    elif validasi_status == "ambisius":

        lines.append(
            f"⚡ Target IPK {target_ipk:.2f} cukup ambisius, "
            "tetapi masih memungkinkan jika kamu konsisten."
        )

    else:

        lines.append(
            f"💡 Target IPK {target_ipk:.2f} perlu disesuaikan "
            "agar lebih realistis dan sehat secara akademik."
        )

    # STRATEGI BELAJAR
    lines.append("\n📚 Strategi Belajar:")

    if kebiasaan == "rutin":

        lines.append(
            "• Kebiasaan belajar rutinmu adalah aset besar. "
            "Tingkatkan kualitas fokus dan evaluasi mingguan."
        )

        lines.append(
            "• Buat jadwal review materi setiap akhir minggu."
        )

    elif kebiasaan == "kadang":

        lines.append(
            "• Mulai bangun rutinitas belajar minimal "
            "1.5 jam setiap hari."
        )

        lines.append(
            "• Gunakan teknik spaced repetition "
            "agar materi lebih mudah diingat."
        )

    else:

        lines.append(
            "• Prioritas utama: bangun kebiasaan belajar "
            "minimal 45 menit setiap hari."
        )

        lines.append(
            "• Cari study buddy atau kelompok belajar "
            "agar lebih konsisten."
        )

    # GAYA BELAJAR
    gaya_label = nama_gaya.get(gaya, gaya)

    lines.append(
        f"\n🧠 Tips untuk Gaya Belajar {gaya_label.title()}:"
    )

    if gaya == "visual":

        lines.append(
            "• Buat mind map untuk setiap bab materi kuliah."
        )

        lines.append(
            "• Gunakan warna berbeda untuk konsep berbeda."
        )

        lines.append(
            "• Manfaatkan video tutorial dan infografis."
        )

    elif gaya == "membaca":

        lines.append(
            "• Buat ringkasan tertulis setelah belajar."
        )

        lines.append(
            "• Gunakan metode Cornell Notes."
        )

        lines.append(
            "• Baca ulang catatan 24 jam setelah kuliah."
        )

    elif gaya == "diskusi":

        lines.append(
            "• Bentuk kelompok belajar 3-4 orang."
        )

        lines.append(
            "• Gunakan teknik teach back."
        )

        lines.append(
            "• Aktif bertanya di kelas."
        )

    else:

        lines.append(
            "• Prioritaskan soal latihan dan studi kasus."
        )

        lines.append(
            "• Ikuti praktikum tambahan jika memungkinkan."
        )

        lines.append(
            "• Buat proyek mini untuk latihan."
        )

    # MATA KULIAH SULIT
    if matkul_tersulit:

        matkul_str = ", ".join(matkul_tersulit[:3])

        lines.append(
            f"\n⚠️ Fokus Mata Kuliah Sulit ({matkul_str}):"
        )

        lines.append(
            "• Alokasikan 40% waktu belajar "
            "untuk mata kuliah tersebut."
        )

        lines.append(
            "• Konsultasi dengan dosen/asisten dosen "
            "minimal 1x per minggu."
        )

        lines.append(
            "• Kerjakan latihan soal dari tahun sebelumnya."
        )

        lines.append(
            "• Jangan menunda belajar hingga mendekati ujian."
        )

    # PENUTUP
    lines.append(
        "\n✨ Ingat: IPK adalah maraton, bukan sprint. "
        "Konsistensi kecil setiap hari lebih penting "
        "daripada belajar berlebihan menjelang ujian."
    )

    return "\n".join(lines)


# ─── BAGIAN 4: MAIN ANALYSIS FUNCTION ────────────────────────────────────


def analyze_ipk_target(
    student,
    prediksi,
    target_ipk,
    kebiasaan_belajar,
    gaya_belajar,
    beban_sks,
    matkul_tersulit
):
    """
    Analisis lengkap target IPK
    """

    current_ipk = student["ipk_kumulatif"]

    semester_aktif = student.get("semester_aktif", 3)

    sisa_semester = max(
        1,
        TOTAL_SEMESTER - semester_aktif + 1
    )

    # Total SKS lulus
    riwayat = student.get("riwayat_semester", [])

    sks_lulus = sum(
        s["sks"]
        for s in riwayat
        if s["semester"] < semester_aktif
    )

    # Prediksi IPK
    pred_ipk = prediksi.get(
        "predicted_ipk",
        current_ipk
    )

    # Validasi target
    validasi = _validasi_target(
        target_ipk,
        current_ipk,
        pred_ipk,
        sisa_semester
    )

    # IPS minimum
    ips_min = _ips_minimum(
        target_ipk,
        current_ipk,
        sks_lulus,
        sisa_semester
    )

    # Proyeksi IPK
    proyeksi = _proyeksi_ipk(
        current_ipk,
        sks_lulus,
        ips_min,
        sisa_semester
    )

    # Estimasi semester tercapai
    sem_capai = None

    for row in proyeksi:

        if row["ipk_proyeksi"] >= target_ipk:

            sem_capai = (
                semester_aktif +
                row["semester_ke"] - 1
            )

            break

    # Panduan personal
    panduan = _panduan_personal(
        target_ipk=target_ipk,
        current_ipk=current_ipk,
        validasi_status=validasi["status"],
        kebiasaan=kebiasaan_belajar,
        gaya=gaya_belajar,
        matkul_tersulit=matkul_tersulit,
        sisa_semester=sisa_semester,
        ips_min=ips_min,
        pred_ipk=pred_ipk
    )

    return {
        "target_ipk": target_ipk,
        "ipk_saat_ini": current_ipk,
        "ipk_prediksi": pred_ipk,
        "sisa_semester": sisa_semester,
        "validasi": validasi,
        "ips_minimum_per_semester": ips_min,
        "proyeksi_ipk": proyeksi,
        "estimasi_semester_capai_target": sem_capai,
        "panduan_personal": panduan
    }
