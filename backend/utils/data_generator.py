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

INDONESIAN_MALE_NAMES = [
    "Ahmad Fauzi", "Budi Santoso", "Cahyo Nugroho", "Deni Firmansyah", "Eko Prasetyo",
    "Fajar Hidayat", "Galih Pramudya", "Hendra Wijaya", "Ivan Kurniawan", "Joko Susilo",
    "Kevin Maulana", "Lukman Hakim", "Muhammad Rizki", "Nanda Pratama", "Oscar Damanik",
    "Putra Ramadhan", "Rizal Mahendra", "Surya Adiputra", "Teguh Wibowo", "Umar Sidik",
    "Vino Ardian", "Wahyu Setiawan", "Yoga Saputra", "Zulfikar Amir", "Arif Budiman",
    "Bagas Wicaksono", "Chandra Darmawan", "Dimas Aditya", "Erwin Saleh", "Faisal Hidayatullah",
    "Gilang Ramadhan", "Haris Munandar", "Ilham Akbar", "Jefri Sitorus", "Khairul Anwar",
    "Leo Saputra", "Muhamad Iqbal", "Novan Setiadi", "Oktavian Putra", "Pandu Wibisono",
    "Rangga Adinugraha", "Stevanus Halim", "Taufik Hidayat", "Victor Manihuruk", "Wendi Supriadi",
    "Yogi Permana", "Aldy Pratama", "Bambang Irawan", "Cakra Wibawa", "Dhika Anggara",
    "Elfan Syahputra", "Fikri Ramadhan", "Hamdan Kusuma", "Irfan Habibi", "Krisna Wardana",
    "Miftah Anwar", "Naufal Arkan", "Rafi Kusuma", "Satria Nugroho", "Tomy Heryanto",
    "Usman Harun", "Vicky Erlangga", "Wahid Fatoni", "Yudha Pratama", "Zakaria Shodiq",
    "Andre Prayogi", "Brian Hartanto", "Dany Kusuma", "Edo Pratama", "Ferdi Wijaksono",
    "Gibran Syahril", "Hendi Surbakti", "Ical Maulana", "Jumadi Waluyo", "Kamal Firmansyah",
    "Lendo Sanjaya", "Mirza Ardiansyah", "Nino Setiawan", "Opi Saputra", "Reza Julianto",
    "Sandy Kurniawan", "Tian Cahyono", "Ujang Suparman", "Valdi Prasetiyo", "Wira Mandala",
    "Yohanes Sitompul", "Zaki Rahman", "Agung Triadi", "Benny Hartono", "Cepi Sujana",
    "Dendy Kuswoyo", "Eri Yunianto", "Frans Sidabutar", "Ganda Hutabarat", "Hano Wirasto",
    "Iman Hamdani", "Jarwo Setiyono", "Kukuh Santoso", "Lukas Permana", "Manu Kristianto",
]

INDONESIAN_FEMALE_NAMES = [
    "Ayu Lestari", "Bella Safitri", "Citra Dewi", "Dewi Rahayu", "Eka Wahyuni",
    "Fitri Handayani", "Gita Nirmala", "Hana Puspita", "Indah Permatasari", "Juwita Sari",
    "Kartika Wulandari", "Laila Nurhayati", "Maya Anggraini", "Nita Kurniawati", "Okta Pratiwi",
    "Putri Ramadhani", "Rina Susanti", "Sari Purnama", "Tika Andriani", "Uswatun Hasanah",
    "Vina Rahmawati", "Wulan Sari", "Yuni Astuti", "Zahira Fadhilah", "Amelia Rosita",
    "Bunga Melati", "Cantika Pramudia", "Dinda Novitasari", "Evi Susilawati", "Farida Hanum",
    "Gina Marlina", "Hasna Widiasari", "Ika Setiowati", "Jihan Azzahra", "Karina Dewantari",
    "Listia Maharani", "Mega Tri Utami", "Novia Ningsih", "Okti Kurniasih", "Peni Lestari",
    "Rara Wulandari", "Silvia Anggraeni", "Tanti Rahmadani", "Ulin Nuha", "Vira Kusumawati",
    "Widya Astuti", "Yani Permatasari", "Zulfa Auliya", "Anisa Rahmawati", "Baiq Sulistiana",
    "Cahyani Pratiwi", "Deva Maulida", "Elsa Permata", "Febriyanti Saputri", "Giana Laksmi",
    "Hilda Noviyanti", "Isna Khoirunisa", "Jesica Manurung", "Khairun Nisa", "Lina Marlina",
    "Meisya Agustina", "Nabilah Salsabila", "Pramesthi Dewi", "Qurrotul Aini", "Reni Oktaviani",
    "Shinta Permata", "Tiara Agustin", "Ulfah Nur Hidayah", "Violeta Santika", "Wiwit Andriyani",
    "Yolanda Kristina", "Zara Amelia", "Agustina Welas", "Bela Rizqiana", "Chika Ramadhani",
    "Desi Kurniawati", "Erlinda Sari", "Fany Maulidia", "Grace Siahaan", "Herlin Situmorang",
    "Irna Hayati", "Jayanti Rahayu", "Kinanti Purnomo", "Luthfia Azzahra", "Mita Andriani",
    "Nayla Kusuma", "Oky Pratiwi", "Pita Wulandari", "Riska Permatasari", "Safira Ramadhani",
    "Trisna Wati", "Ulfa Khairani", "Vanny Aprilia", "Wahyuni Rahayu", "Yunita Sari",
    "Zahra Nabilah", "Adinda Cahyani", "Binti Masruroh", "Clara Devita", "Diah Ayu Lestari",
]


def seeded_random(seed_str: str, salt: str = "") -> random.Random:
    """Create a seeded Random instance."""
    h = hashlib.md5(f"{seed_str}{salt}".encode()).hexdigest()
    seed_val = int(h[:8], 16)
    return random.Random(seed_val)


# Performance profiles: IPK ranges and grade distributions
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

GRADE_TO_ANGKA = {"A": 4.0, "AB": 3.5, "B": 3.0, "BC": 2.5, "C": 2.0, "D": 1.0, "E": 0.0}

# Distribution per prodi: 4+6+7+5+2+1 = 25
PERFORMANCE_DISTRIBUTION = (
    ["sangat_berprestasi"] * 4 +
    ["berprestasi"] * 6 +
    ["baik"] * 7 +
    ["cukup"] * 5 +
    ["kurang"] * 2 +
    ["berisiko"] * 1
)


def pick_grade(rng: random.Random, profile: str) -> str:
    """Pick a grade letter based on profile weights."""
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


def select_courses_for_semester(prodi_key: str, semester: int, rng: random.Random, target_sks: int) -> list:
    """
    Select courses for a semester:
    - Always take all wajib courses
    - Fill electives until reaching target_sks
    - Shuffle electives with seeded random for variety
    """
    wajib = get_wajib_courses(prodi_key, semester)
    pilihan = get_pilihan_courses(prodi_key, semester)

    selected = list(wajib)
    current_sks = sum(c["sks"] for c in selected)

    # Shuffle electives
    shuffled_pilihan = list(pilihan)
    rng.shuffle(shuffled_pilihan)

    for course in shuffled_pilihan:
        if current_sks >= target_sks:
            break
        selected.append(course)
        current_sks += course["sks"]

    return selected


def recommended_sks_for_profile(profile: str) -> int:
    """Get recommended SKS based on performance profile."""
    mapping = {
        "sangat_berprestasi": 24,
        "berprestasi": 24,
        "baik": 23,
        "cukup": 22,
        "kurang": 21,
        "berisiko": 21,
    }
    return mapping.get(profile, 22)


def generate_student(nim: str, nama: str, jenis_kelamin: str, prodi_key: str, profile: str) -> dict:
    """Generate a single student record."""
    prodi_info = CURRICULUM[prodi_key]
    prodi_name = prodi_info["name"]

    riwayat = []
    cumulative_sks = 0
    cumulative_points = 0.0

    target_sks_per_sem = recommended_sks_for_profile(profile)

    for sem in [1, 2, 3]:
        # Use seeded rng per semester
        rng = seeded_random(nim, f"sem_{sem}")

        # Select courses
        selected_courses = select_courses_for_semester(prodi_key, sem, rng, target_sks_per_sem)

        # Generate grades for each course
        nilai_list = []
        for course in selected_courses:
            grade_rng = seeded_random(nim, f"grade_{sem}_{course['kode']}")
            # Add slight semester progression
            effective_profile = profile
            # For some profiles, slight variation by semester
            if profile == "berprestasi" and sem == 3:
                r = grade_rng.random()
                if r < 0.3:
                    effective_profile = "sangat_berprestasi"
            elif profile == "baik" and sem == 1:
                r = grade_rng.random()
                if r < 0.2:
                    effective_profile = "cukup"

            nilai_huruf = pick_grade(grade_rng, effective_profile)
            nilai_angka = GRADE_TO_ANGKA[nilai_huruf]

            nilai_list.append({
                "kode": course["kode"],
                "nama": course["nama"],
                "sks": course["sks"],
                "nilai_huruf": nilai_huruf,
                "nilai_angka": nilai_angka,
            })

        # Calculate actual IPS from grades
        sem_sks = sum(n["sks"] for n in nilai_list)
        if sem_sks > 0:
            actual_ips = sum(n["nilai_angka"] * n["sks"] for n in nilai_list) / sem_sks
        else:
            actual_ips = 0.0
        actual_ips = round(actual_ips, 2)

        cumulative_sks += sem_sks
        cumulative_points += actual_ips * sem_sks

        riwayat.append({
            "semester": sem,
            "ips": actual_ips,
            "sks": sem_sks,
            "nilai_matkul": nilai_list,
        })

    ipk_kumulatif = round(cumulative_points / cumulative_sks, 2) if cumulative_sks > 0 else 0.0

    return {
        "nim": nim,
        "nama": nama,
        "prodi": prodi_name,
        "prodi_key": prodi_key,
        "angkatan": 2024,
        "jenis_kelamin": jenis_kelamin,
        "semester_aktif": 3,
        "ipk_kumulatif": ipk_kumulatif,
        "riwayat_semester": riwayat,
    }


def generate_all_students() -> list:
    """Generate all 100 students (25 per prodi)."""
    prodi_configs = [
        ("TI", "024"),
        ("AK", "025"),
        ("TM", "026"),
        ("AP", "027"),
    ]

    male_names = INDONESIAN_MALE_NAMES[:]
    female_names = INDONESIAN_FEMALE_NAMES[:]

    students = []
    used_names = set()

    for prodi_key, prodi_code in prodi_configs:
        rng_prodi = seeded_random(f"prodi_{prodi_code}")
        perf_list = PERFORMANCE_DISTRIBUTION[:]
        rng_prodi.shuffle(perf_list)

        avail_male = [n for n in male_names if n not in used_names]
        avail_female = [n for n in female_names if n not in used_names]

        for seq in range(1, 26):
            nim = f"24{prodi_code}{seq:03d}"
            profile = perf_list[seq - 1]

            rng_student = seeded_random(nim)
            is_male = rng_student.random() < 0.5

            if is_male and avail_male:
                idx = rng_student.randint(0, len(avail_male) - 1)
                nama = avail_male[idx]
                avail_male = [n for i, n in enumerate(avail_male) if i != idx]
                used_names.add(nama)
            elif avail_female:
                idx = rng_student.randint(0, len(avail_female) - 1)
                nama = avail_female[idx]
                avail_female = [n for i, n in enumerate(avail_female) if i != idx]
                used_names.add(nama)
                is_male = False
            else:
                nama = f"Mahasiswa {nim}"
                is_male = True

            jenis_kelamin = "L" if is_male else "P"
            student = generate_student(nim, nama, jenis_kelamin, prodi_key, profile)
            students.append(student)

    return students


def save_students_json(output_path: str) -> None:
    """Generate and save students to JSON file."""
    students = generate_all_students()
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(students)} students -> {output_path}")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output = os.path.join(base_dir, "students.json")
    save_students_json(output)
