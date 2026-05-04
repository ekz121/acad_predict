# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 1: IMPORT & CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════
from math import ceil

TOTAL_SEMESTER = 6
SKS_PER_SEMESTER = 22


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 2: HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════

def _ips_minimum(target_ipk, current_ipk, sks_lulus, sisa_semester) -> float:
    sks_sisa = sisa_semester * SKS_PER_SEMESTER
    total_sks = sks_lulus + sks_sisa

    if sks_sisa > 0:
        ips_min = (target_ipk * total_sks - current_ipk * sks_lulus) / sks_sisa
    else:
        ips_min = 0.0

    return round(max(0.0, min(4.0, ips_min)), 2)


def _proyeksi_ipk(current_ipk, sks_lulus, ips_per_sem, sisa_semester) -> list:
    rows = []
    ipk = current_ipk
    sks = sks_lulus

    for i in range(1, sisa_semester + 1):
        sks += SKS_PER_SEMESTER
        ipk = round(
            (ipk * (sks - SKS_PER_SEMESTER) + ips_per_sem * SKS_PER_SEMESTER) / sks,
            2
        )
        rows.append({
            "semester_ke": i,
            "ipk_proyeksi": ipk
        })

    return rows


def _validasi_target(target_ipk, current_ipk, pred_ipk, sisa_semester) -> dict:
    if target_ipk > 4.0:
        return {
            "status": "tidak_valid",
            "label": "Tidak Valid",
            "pesan": "Target IPK tidak boleh melebihi 4.00."
        }

    ips_min = _ips_minimum(target_ipk, current_ipk, 0, sisa_semester)

    if ips_min > 4.0:
        return {
            "status": "tidak_mungkin",
            "label": "Tidak Mungkin",
            "pesan": "Target IPK tidak dapat dicapai dengan sisa semester yang ada."
        }

    gap = target_ipk - current_ipk

    if gap <= 0.05:
        return {
            "status": "realistis",
            "label": "Realistis ✓",
            "pesan": "Target sudah sesuai dengan kondisi saat ini."
        }

    if ips_min <= 3.5 and sisa_semester >= 2:
        return {
            "status": "realistis",
            "label": "Realistis ✓",
            "pesan": "Target dapat dicapai dengan performa stabil."
        }

    if ips_min <= 4.0 and sisa_semester >= 1:
        return {
            "status": "ambisius",
            "label": "Ambisius ⚡",
            "pesan": "Target ambisius, butuh usaha ekstra konsisten."
        }

    return {
        "status": "tidak_mungkin",
        "label": "Tidak Mungkin ✗",
        "pesan": "Target terlalu tinggi untuk dicapai."
    }


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 3: PANDUAN PERSONAL GENERATOR
# ═══════════════════════════════════════════════════════════════════════════

def _panduan_personal(target_ipk, current_ipk, validasi_status,
                     kebiasaan, gaya, matkul_tersulit,
                     sisa_semester, ips_min, pred_ipk) -> str:

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

    # Pembuka
    if validasi_status == "realistis":
        lines.append(f"🎯 Target IPK {target_ipk:.2f} sangat realistis untukmu!")
    elif validasi_status == "ambisius":
        lines.append(f"⚡ Target IPK {target_ipk:.2f} cukup ambisius, tapi masih bisa dicapai!")
    else:
        lines.append(f"💡 Target IPK {target_ipk:.2f} perlu disesuaikan agar lebih realistis.")

    # Strategi belajar
    lines.append("\n📚 Strategi Belajar:")

    if kebiasaan == "rutin":
        lines.append("• Kebiasaan belajar rutinmu adalah aset besar. Tingkatkan kualitas belajar.")
        lines.append("• Buat jadwal review mingguan untuk konsistensi.")
    elif kebiasaan == "kadang":
        lines.append("• Bangun rutinitas belajar minimal 1.5 jam per hari.")
        lines.append("• Gunakan teknik spaced repetition.")
    else:
        lines.append("• Prioritas utama: bangun kebiasaan belajar minimal 45 menit per hari.")
        lines.append("• Cari study buddy atau kelompok belajar.")

    # Gaya belajar
    gaya_nama = nama_gaya.get(gaya, gaya)
    lines.append(f"\n🧠 Tips untuk Gaya Belajar {gaya_nama.title()}:")

    if gaya == "visual":
        lines.append("• Gunakan mind map dan diagram.")
        lines.append("• Gunakan warna berbeda untuk konsep.")
        lines.append("• Tonton video pembelajaran.")
    elif gaya == "membaca":
        lines.append("• Buat ringkasan setelah belajar.")
        lines.append("• Gunakan Cornell Notes.")
        lines.append("• Review dalam 24 jam.")
    elif gaya == "diskusi":
        lines.append("• Bentuk kelompok belajar kecil.")
        lines.append("• Gunakan teknik teach-back.")
        lines.append("• Aktif bertanya.")
    else:
        lines.append("• Fokus latihan soal dan praktik.")
        lines.append("• Ikuti proyek tambahan.")
        lines.append("• Buat mini project.")

    # Mata kuliah sulit
    if matkul_tersulit:
        matkul_str = ", ".join(matkul_tersulit[:3])
        lines.append(f"\n⚠️ Fokus Mata Kuliah Sulit ({matkul_str}):")
        lines.append("• Alokasikan 40% waktu belajar.")
        lines.append("• Konsultasi rutin dengan dosen.")
        lines.append("• Kerjakan soal latihan intensif.")
        lines.append("• Mulai dari awal semester.")

    # Penutup
    lines.append("\n✨ Ingat: IPK adalah maraton, bukan sprint. Konsistensi adalah kunci utama.")

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════════
# BAGIAN 4: MAIN FUNCTION
# ═══════════════════════════════════════════════════════════════════════════

def analyze_ipk_target(student, prediksi, target_ipk,
                       kebiasaan_belajar, gaya_belajar,
                       beban_sks, matkul_tersulit):

    current_ipk = student["ipk_kumulatif"]
    semester_aktif = student.get("semester_aktif", 3)
    sisa_semester = max(1, TOTAL_SEMESTER - semester_aktif + 1)

    riwayat = student.get("riwayat_semester", [])
    sks_lulus = sum(s["sks"] for s in riwayat if s["semester"] < semester_aktif)

    pred_ipk = prediksi.get("predicted_ipk", current_ipk)

    validasi = _validasi_target(target_ipk, current_ipk, pred_ipk, sisa_semester)

    ips_min = _ips_minimum(target_ipk, current_ipk, sks_lulus, sisa_semester)

    proyeksi = _proyeksi_ipk(current_ipk, sks_lulus, ips_min, sisa_semester)

    sem_capai = None
    for row in proyeksi:
        if row["ipk_proyeksi"] >= target_ipk:
            sem_capai = semester_aktif + row["semester_ke"] - 1
            break

    panduan = _panduan_personal(
        target_ipk, current_ipk,
        validasi["status"],
        kebiasaan_belajar,
        gaya_belajar,
        matkul_tersulit,
        sisa_semester,
        ips_min,
        pred_ipk
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
