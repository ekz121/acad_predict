"""
Analisis Target IPK: matematis + panduan personal.
"""
from math import ceil


TOTAL_SEMESTER = 6
SKS_PER_SEMESTER = 22  # estimasi rata-rata


def _ips_minimum(target_ipk: float, current_ipk: float, sks_lulus: int, sisa_semester: int) -> float:
    """Hitung IPS minimum rata-rata yang harus dicapai tiap sisa semester."""
    sks_sisa = sisa_semester * SKS_PER_SEMESTER
    total_sks = sks_lulus + sks_sisa
    ips_min = (target_ipk * total_sks - current_ipk * sks_lulus) / sks_sisa if sks_sisa > 0 else 0.0
    return round(max(0.0, min(4.0, ips_min)), 2)


def _proyeksi_ipk(current_ipk: float, sks_lulus: int, ips_per_sem: float, sisa_semester: int) -> list:
    """Proyeksi IPK per semester ke depan."""
    rows = []
    ipk = current_ipk
    sks = sks_lulus
    for i in range(1, sisa_semester + 1):
        sks += SKS_PER_SEMESTER
        ipk = round((ipk * (sks - SKS_PER_SEMESTER) + ips_per_sem * SKS_PER_SEMESTER) / sks, 2)
        rows.append({"semester_ke": i, "ipk_proyeksi": ipk})
    return rows


def _validasi_target(target_ipk: float, current_ipk: float, pred_ipk: float, sisa_semester: int) -> dict:
    """Tentukan apakah target realistis."""
    if target_ipk > 4.0:
        return {"status": "tidak_valid", "label": "Tidak Valid", "pesan": "Target IPK tidak boleh melebihi 4.00."}

    ips_min = _ips_minimum(target_ipk, current_ipk, 0, sisa_semester)  # rough check
    if ips_min > 4.0:
        return {"status": "tidak_mungkin", "label": "Tidak Mungkin", "pesan": f"Target {target_ipk:.2f} tidak dapat dicapai meski IPS 4.00 setiap semester."}

    gap = target_ipk - current_ipk
    if gap <= 0.05:
        return {"status": "realistis", "label": "Realistis ✓", "pesan": "Target sudah sesuai atau sedikit di atas IPK saat ini. Pertahankan performa!"}
    if ips_min <= 3.5 and sisa_semester >= 2:
        return {"status": "realistis", "label": "Realistis ✓", "pesan": f"Target dapat dicapai dengan IPS minimum {ips_min:.2f} per semester."}
    if ips_min <= 4.0 and sisa_semester >= 1:
        return {"status": "ambisius", "label": "Ambisius ⚡", "pesan": f"Target ambisius — butuh IPS {ips_min:.2f} per semester. Perlu kerja keras ekstra."}
    return {"status": "tidak_mungkin", "label": "Tidak Mungkin ✗", "pesan": "Target terlalu tinggi untuk dicapai dalam sisa semester yang ada."}


def _panduan_personal(
    target_ipk: float,
    current_ipk: float,
    validasi_status: str,
    kebiasaan: str,
    gaya: str,
    matkul_tersulit: list,
    sisa_semester: int,
    ips_min: float,
    pred_ipk: float,
) -> str:
    nama_gaya = {"visual": "visual (diagram/mind map)", "membaca": "membaca & mencatat", "diskusi": "diskusi kelompok", "praktek": "praktek langsung"}.get(gaya, gaya)
    nama_kebiasaan = {"rutin": "rutin setiap hari", "kadang": "kadang-kadang", "jarang": "jarang belajar"}.get(kebiasaan, kebiasaan)

    lines = []

    # Pembuka motivasi
    if validasi_status == "realistis":
        lines.append(f"🎯 Target IPK {target_ipk:.2f} sangat realistis untukmu! Dengan IPK saat ini {current_ipk:.2f} dan {sisa_semester} semester tersisa, kamu berada di jalur yang tepat.")
    elif validasi_status == "ambisius":
        lines.append(f"⚡ Target IPK {target_ipk:.2f} cukup ambisius, tapi bukan tidak mungkin! Kamu perlu meningkatkan IPS menjadi minimal {ips_min:.2f} setiap semester. Tantangan ini bisa kamu taklukkan!")
    else:
        lines.append(f"💡 Target IPK {target_ipk:.2f} perlu disesuaikan. Berdasarkan data, target yang lebih realistis adalah sekitar {min(pred_ipk + 0.2, 4.0):.2f}. Jangan menyerah — fokus pada peningkatan bertahap!")

    # Strategi berdasarkan kebiasaan belajar
    lines.append("\n📚 Strategi Belajar:")
    if kebiasaan == "rutin":
        lines.append("• Kebiasaan belajar rutinmu adalah aset besar. Tingkatkan kualitas sesi belajar dengan teknik Pomodoro (25 menit fokus, 5 menit istirahat).")
        lines.append("• Buat jadwal review mingguan untuk semua mata kuliah, bukan hanya menjelang ujian.")
    elif kebiasaan == "kadang":
        lines.append("• Mulai bangun rutinitas belajar minimal 1.5 jam per hari. Konsistensi lebih penting dari durasi panjang yang tidak teratur.")
        lines.append("• Gunakan teknik spaced repetition — ulangi materi di hari ke-1, ke-3, ke-7 setelah belajar.")
    else:
        lines.append("• Prioritas utama: bangun kebiasaan belajar harian minimal 45 menit. Mulai kecil, tapi konsisten.")
        lines.append("• Cari study buddy atau bergabung kelompok belajar untuk meningkatkan motivasi dan akuntabilitas.")

    # Tips berdasarkan gaya belajar
    lines.append(f"\n🧠 Tips untuk Gaya Belajar {nama_gaya.title()}:")
    if gaya == "visual":
        lines.append("• Buat mind map untuk setiap bab materi kuliah.")
        lines.append("• Gunakan warna berbeda untuk konsep berbeda saat mencatat.")
        lines.append("• Manfaatkan video tutorial dan infografis sebagai suplemen belajar.")
    elif gaya == "membaca":
        lines.append("• Buat ringkasan tertulis setelah setiap sesi belajar — ini memperkuat retensi.")
        lines.append("• Gunakan metode Cornell Notes untuk mencatat kuliah secara sistematis.")
        lines.append("• Baca ulang catatan 24 jam setelah kuliah untuk memperkuat memori.")
    elif gaya == "diskusi":
        lines.append("• Bentuk kelompok belajar 3-4 orang untuk diskusi rutin setiap minggu.")
        lines.append("• Coba teknik 'teach back' — jelaskan materi ke teman untuk menguji pemahamanmu.")
        lines.append("• Aktif bertanya di kelas dan forum diskusi online.")
    else:  # praktek
        lines.append("• Prioritaskan mengerjakan soal latihan dan studi kasus sebanyak mungkin.")
        lines.append("• Ikuti praktikum atau proyek tambahan yang relevan dengan mata kuliah.")
        lines.append("• Buat proyek mini untuk mengaplikasikan teori yang dipelajari.")

    # Prioritas mata kuliah sulit
    if matkul_tersulit:
        matkul_str = ", ".join(matkul_tersulit[:3])
        lines.append(f"\n⚠️ Fokus Mata Kuliah Sulit ({matkul_str}):")
        lines.append("• Alokasikan 40% waktu belajar untuk mata kuliah ini.")
        lines.append("• Konsultasi ke dosen atau asisten dosen minimal 1x per minggu.")
        lines.append("• Kerjakan semua soal latihan dari tahun-tahun sebelumnya.")
        lines.append("• Jangan tunda — mulai belajar dari minggu pertama, bukan menjelang UTS/UAS.")

    # Penutup
    lines.append(f"\n✨ Ingat: IPK adalah maraton, bukan sprint. Setiap nilai yang kamu perbaiki, sekecil apapun, membawa kamu lebih dekat ke target {target_ipk:.2f}. Semangat!")

    return "\n".join(lines)


def analyze_ipk_target(
    student: dict,
    prediksi: dict,
    target_ipk: float,
    kebiasaan_belajar: str,
    gaya_belajar: str,
    beban_sks: int,
    matkul_tersulit: list,
) -> dict:
    current_ipk = student["ipk_kumulatif"]
    semester_aktif = student.get("semester_aktif", 3)
    sisa_semester = max(1, TOTAL_SEMESTER - semester_aktif + 1)

    # Hitung total SKS yang sudah lulus
    riwayat = student.get("riwayat_semester", [])
    sks_lulus = sum(s["sks"] for s in riwayat if s["semester"] < semester_aktif)

    pred_ipk = prediksi.get("prediksi_ipk_baru", current_ipk)

    # Validasi target
    validasi = _validasi_target(target_ipk, current_ipk, pred_ipk, sisa_semester)

    # IPS minimum yang harus dicapai
    ips_min = _ips_minimum(target_ipk, current_ipk, sks_lulus, sisa_semester)

    # Proyeksi IPK per semester
    proyeksi = _proyeksi_ipk(current_ipk, sks_lulus, ips_min, sisa_semester)

    # Estimasi semester untuk capai target (cari semester pertama proyeksi >= target)
    sem_capai = None
    for row in proyeksi:
        if row["ipk_proyeksi"] >= target_ipk:
            sem_capai = semester_aktif + row["semester_ke"] - 1
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
        pred_ipk=pred_ipk,
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
        "panduan_personal": panduan,
    }
