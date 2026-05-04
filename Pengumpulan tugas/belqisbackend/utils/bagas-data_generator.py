"""
Generate 100 synthetic student records (25 per prodi).
semester_aktif = 3 (students have completed semesters 1, 2, 3).
prediction_target = 4.
"""

import json
import random
import os
import hashlib
from .curriculum import CURRICULUM, get_wajib_courses, get_pilihan_courses


# ============================================================================
# CONSTANTS
# ============================================================================

INDONESIAN_MALE_NAMES = [
    "Ahmad Fauzi","Budi Santoso","Cahyo Nugroho","Dedi Kurniawan","Eko Prasetyo",
    "Fajar Hidayat","Gilang Ramadhan","Hendra Wijaya","Irfan Maulana","Joko Susilo",
    "Kurniawan Saputra","Lukman Hakim","Muhammad Rizki","Nanda Pratama","Oki Setiawan",
    "Putra Wijaya","Rizal Fahmi","Sandi Pratama","Teguh Santoso","Umar Faruq",
    "Vicky Prasetyo","Wahyu Hidayat","Yoga Pratama","Zaki Mubarak"
] * 4  # jadi 100

INDONESIAN_FEMALE_NAMES = [
    "Ayu Lestari","Bella Safitri","Citra Dewi","Dewi Sartika","Eka Putri",
    "Fitriani","Gita Sari","Hani Nuraini","Indah Permata","Jihan Rahma",
    "Kartika Sari","Lina Marlina","Maya Sari","Nina Oktaviani","Oktavia Putri",
    "Putri Ayu","Qori Rahma","Rina Sari","Siti Aisyah","Tika Lestari",
    "Umi Kalsum","Vina Oktavia","Wulan Sari","Yuni Kartika","Zahra Nabila"
] * 4


PERFORMANCE_PROFILES = {
    "sangat_berprestasi": {
        "ipk_range": (3.75, 4.00),
        "grade_weights": {"A": 0.70, "AB": 0.25, "B": 0.05, "BC": 0.0, "C": 0.0, "D": 0.0, "E": 0.0},
    },
    "berprestasi": {
        "ipk_range": (3.50, 3.74),
        "grade_weights": {"A": 0.40, "AB": 0.40, "B": 0.15, "BC": 0.05, "C": 0.0, "D": 0.0, "E": 0.0},
    },
    "baik": {
        "ipk_range": (3.00, 3.49),
        "grade_weights": {"A": 0.15, "AB": 0.30, "B": 0.40, "BC": 0.10, "C": 0.05, "D": 0.0, "E": 0.0},
    },
    "cukup": {
        "ipk_range": (2.50, 2.99),
        "grade_weights": {"A": 0.05, "AB": 0.10, "B": 0.35, "BC": 0.35, "C": 0.15, "D": 0.0, "E": 0.0},
    },
    "kurang": {
        "ipk_range": (2.00, 2.49),
        "grade_weights": {"A": 0.0, "AB": 0.05, "B": 0.20, "BC": 0.35, "C": 0.30, "D": 0.10, "E": 0.0},
    },
    "berisiko": {
        "ipk_range": (1.50, 1.99),
        "grade_weights": {"A": 0.0, "AB": 0.0, "B": 0.05, "BC": 0.20, "C": 0.40, "D": 0.25, "E": 0.10},
    },
}

GRADE_TO_ANGKA = {
    "A": 4.0, "AB": 3.5, "B": 3.0,
    "BC": 2.5, "C": 2.0, "D": 1.0, "E": 0.0
}

PERFORMANCE_DISTRIBUTION = (
    ["sangat_berprestasi"] * 4 +
    ["berprestasi"] * 6 +
    ["baik"] * 7 +
    ["cukup"] * 5 +
    ["kurang"] * 2 +
    ["berisiko"] * 1
)


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def seeded_random(seed_str: str, salt: str = "") -> random.Random:
    h = hashlib.md5(f"{seed_str}{salt}".encode()).hexdigest()
    seed_val = int(h[:8], 16)
    return random.Random(seed_val)


def pick_grade(rng: random.Random, profile: str) -> str:
    weights = PERFORMANCE_PROFILES[profile]["grade_weights"]
    grades = list(weights.keys())
    probs = list(weights.values())

    r = rng.random()
    cumulative = 0.0
    for g, p in zip(grades, probs):
        cumulative += p
        if r <= cumulative:
            return g
    return grades[-1]


def select_courses_for_semester(prodi_key, semester, rng, target_sks):
    wajib = get_wajib_courses(prodi_key, semester)
    pilihan = get_pilihan_courses(prodi_key, semester)

    selected = list(wajib)
    current_sks = sum(c["sks"] for c in selected)

    shuffled = list(pilihan)
    rng.shuffle(shuffled)

    for c in shuffled:
        if current_sks >= target_sks:
            break
        selected.append(c)
        current_sks += c["sks"]

    return selected


def recommended_sks_for_profile(profile):
    mapping = {
        "sangat_berprestasi": 24,
        "berprestasi": 24,
        "baik": 23,
        "cukup": 22,
        "kurang": 21,
        "berisiko": 21,
    }
    return mapping.get(profile, 22)


# ============================================================================
# MAIN GENERATOR
# ============================================================================

def generate_student(nim, nama, jk, prodi_key, profile):
    prodi_name = CURRICULUM[prodi_key]["name"]

    riwayat = []
    cumulative_sks = 0
    cumulative_points = 0

    target_sks = recommended_sks_for_profile(profile)

    for sem in range(1, 4):
        rng = seeded_random(nim, f"sem_{sem}")
        courses = select_courses_for_semester(prodi_key, sem, rng, target_sks)

        nilai_list = []

        for c in courses:
            grade_rng = seeded_random(nim, f"{sem}_{c['kode']}")
            huruf = pick_grade(grade_rng, profile)
            angka = GRADE_TO_ANGKA[huruf]

            nilai_list.append({
                "kode": c["kode"],
                "nama": c["nama"],
                "sks": c["sks"],
                "nilai_huruf": huruf,
                "nilai_angka": angka
            })

        sem_sks = sum(n["sks"] for n in nilai_list)
        ips = sum(n["nilai_angka"] * n["sks"] for n in nilai_list) / sem_sks
        ips = round(ips, 2)

        cumulative_sks += sem_sks
        cumulative_points += ips * sem_sks

        riwayat.append({
            "semester": sem,
            "ips": ips,
            "sks": sem_sks,
            "nilai_matkul": nilai_list
        })

    ipk = round(cumulative_points / cumulative_sks, 2)

    return {
        "nim": nim,
        "nama": nama,
        "prodi": prodi_name,
        "prodi_key": prodi_key,
        "angkatan": 2024,
        "jenis_kelamin": jk,
        "semester_aktif": 3,
        "ipk_kumulatif": ipk,
        "riwayat_semester": riwayat
    }


def generate_all_students():
    prodi_configs = [
        ("TI", "024"),
        ("AK", "025"),
        ("TM", "026"),
        ("AP", "027"),
    ]

    students = []
    used_names = set()

    male = INDONESIAN_MALE_NAMES[:]
    female = INDONESIAN_FEMALE_NAMES[:]

    for prodi_key, code in prodi_configs:
        rng = seeded_random(code)

        perf = PERFORMANCE_DISTRIBUTION[:]
        rng.shuffle(perf)

        for i in range(1, 26):
            nim = f"24{code}{i:03d}"
            profile = perf[i-1]

            rng_s = seeded_random(nim)
            is_male = rng_s.random() < 0.5

            pool = male if is_male else female
            name = pool.pop(rng_s.randint(0, len(pool)-1))
            used_names.add(name)

            jk = "L" if is_male else "P"

            student = generate_student(nim, name, jk, prodi_key, profile)
            students.append(student)

    return students


def save_students_json(path):
    data = generate_all_students()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(data)} students -> {path}")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output = os.path.join(base, "students.json")
    save_students_json(output)
