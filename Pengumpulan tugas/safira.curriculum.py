# =====================================================
# DATA PRODI
# =====================================================

PRODI_LIST = {
    "TI": {
        "name": "Teknologi Informasi",
        "prodi_code": "100"
    },
    "AK": {
        "name": "Akuntansi",
        "prodi_code": "110"
    },
    "TM": {
        "name": "Teknik Mesin",
        "prodi_code": "120"
    },
    "AP": {
        "name": "Administrasi Perkantoran",
        "prodi_code": "130"
    }
}


# =====================================================
# FUNGSI UNTUK MEMBUAT DATA MATA KULIAH
# =====================================================

def generate_courses(prefix, semester, jumlah_wajib, jumlah_pilihan):
    courses = []

    # ========================
    # MATA KULIAH WAJIB
    # ========================
    for i in range(1, jumlah_wajib + 1):
        course = {
            "kode": prefix + str(semester) + str(i).zfill(2),
            "nama": "Mata Kuliah Wajib " + str(semester) + "-" + str(i),
            "sks": 3,
            "wajib": True
        }
        courses.append(course)

    # ========================
    # MATA KULIAH PILIHAN
    # ========================
    for i in range(1, jumlah_pilihan + 1):
        course = {
            "kode": prefix + str(semester) + "P" + str(i).zfill(2),
            "nama": "Mata Kuliah Pilihan " + str(semester) + "-" + str(i),
            "sks": 2,
            "wajib": False
        }
        courses.append(course)

    return courses


# =====================================================
# MEMBANGUN CURRICULUM
# =====================================================

CURRICULUM = {}

for prodi_key in PRODI_LIST:

    # Ambil data prodi
    prodi_data = PRODI_LIST[prodi_key]

    # Struktur utama
    CURRICULUM[prodi_key] = {
        "name": prodi_data["name"],
        "prodi_code": prodi_data["prodi_code"],
        "semesters": {}
    }

    # Loop semester 1 - 6
    for semester in range(1, 7):

        # ========================
        # PENENTUAN JUMLAH MATKUL
        # ========================
        if semester == 1 or semester == 2:
            jumlah_wajib = 8
            jumlah_pilihan = 9

        elif semester == 3 or semester == 4:
            jumlah_wajib = 6
            jumlah_pilihan = 11

        elif semester == 5:
            jumlah_wajib = 4
            jumlah_pilihan = 10

        elif semester == 6:
            jumlah_wajib = 3
            jumlah_pilihan = 9

        # Generate mata kuliah
        courses = generate_courses(prodi_key, semester, jumlah_wajib, jumlah_pilihan)

        # ========================
        # KHUSUS SEMESTER 6
        # ========================
        if semester == 6:
            courses[0] = {
                "kode": prodi_key + "601",
                "nama": "Tugas Akhir",
                "sks": 6,
                "wajib": True
            }
            courses[1] = {
                "kode": prodi_key + "602",
                "nama": "Kerja Praktek",
                "sks": 3,
                "wajib": True
            }
            courses[2] = {
                "kode": prodi_key + "603",
                "nama": "Seminar",
                "sks": 2,
                "wajib": True
            }

        # Simpan ke curriculum
        CURRICULUM[prodi_key]["semesters"][semester] = courses


# =====================================================
# FUNGSI UTAMA
# =====================================================

def get_wajib_courses(prodi_key, semester) -> list:
    hasil = []
    for course in CURRICULUM[prodi_key]["semesters"][semester]:
        if course["wajib"] == True:
            hasil.append(course)
    return hasil


def get_pilihan_courses(prodi_key, semester) -> list:
    hasil = []
    for course in CURRICULUM[prodi_key]["semesters"][semester]:
        if course["wajib"] == False:
            hasil.append(course)
    return hasil


def get_prodi_key(nim: str) -> str:
    kode = nim[2:5]

    if kode == "100":
        return "TI"
    elif kode == "110":
        return "AK"
    elif kode == "120":
        return "TM"
    elif kode == "130":
        return "AP"
    else:
        return "TI"


def get_max_sks_by_ipk(ipk, semester) -> int:
    if ipk >= 3.0:
        return 24
    elif ipk >= 2.5:
        return 22
    else:
        return 20


def validate_prerequisites(kode, completed) -> tuple[bool, list]:
    prerequisites = {
        "TI20101": ["TI10101"],
        "AK20101": ["AK10101"],
        "TM20101": ["TM10101"],
        "AP20101": ["AP10101"],
    }

    if kode not in prerequisites:
        return True, []

    missing = []

    for pr in prerequisites[kode]:
        if pr not in completed:
            missing.append(pr)

    if len(missing) == 0:
        return True, []
    else:
        return False, missing


def get_completed_courses(riwayat) -> set:
    hasil = set()

    for item in riwayat:
        if item["lulus"] == True:
            hasil.add(item["kode"])

    return hasil
