(utils/__init__.py menyimpan fungsi utilitas (load, save, predict, analyze))

import json
import os

STUDENTS_FILE = "students.json"

def save_students_json():
    """Auto-generate students.json jika tidak ada"""
    sample_students = [
        {"nim": "24024005", "nama": "Belqista", "prodi": "Teknologi Informasi", "ipk": 3.8},
        {"nim": "24022017", "nama": "Naily", "prodi": "Teknologi Mesin", "ipk": 3.8},
        {"nim": "24023007", "nama": "Isna", "prodi": "Akutansi", "ipk": 3.8},
    ]
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(sample_students, f, indent=2)

def load_students_json():
    """Load students.json ke dict cache dengan key = NIM"""
    if not os.path.exists(STUDENTS_FILE):
        save_students_json()
    with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
        students = json.load(f)
    return {s["nim"]: s for s in students}

def predict_student(student: dict):
    """Dummy prediction function"""
    return {
        "prediksi_kelulusan": "Tepat waktu" if student["ipk"] >= 3.0 else "Terlambat",
        "rekomendasi": "Pertahankan konsistensi belajar"
    }

def analyze_ipk_target(nim: str, request):
    """Dummy analysis function"""
    return {
        "nim": nim,
        "target_ipk": request.target_ipk,
        "analisis": f"Dengan kebiasaan {request.kebiasaan_belajar}, gaya {request.gaya_belajar}, "
                    f"dan beban {request.beban_sks_direncanakan} SKS, target IPK {request.target_ipk} "
                    f"masih realistis meski ada tantangan di {request.matkul_tersulit}."
    }
