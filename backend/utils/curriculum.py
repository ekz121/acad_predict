"""
Curriculum definitions for all 4 prodi across 6 semesters.
Each course has 1 or 2 SKS, marked as wajib (mandatory) or pilihan (elective).
Each semester has a pool of 15-18 courses totaling 28-32 SKS.
"""

CURRICULUM = {
    "TI": {
        "name": "Teknologi Informasi",
        "prodi_code": "024",
        "semesters": {
            1: [
                # Wajib (14 SKS)
                {"kode": "TI101", "nama": "Logika Pemrograman", "sks": 2, "wajib": True},
                {"kode": "TI102", "nama": "Algoritma Dasar", "sks": 2, "wajib": True},
                {"kode": "TI103", "nama": "Matematika Diskrit", "sks": 2, "wajib": True},
                {"kode": "TI104", "nama": "Pengantar Teknologi Informasi", "sks": 2, "wajib": True},
                {"kode": "TI105", "nama": "Bahasa Indonesia Akademik", "sks": 1, "wajib": True},
                {"kode": "TI106", "nama": "Bahasa Inggris I", "sks": 2, "wajib": True},
                {"kode": "TI107", "nama": "Pendidikan Agama & Moral", "sks": 2, "wajib": True},
                {"kode": "TI108", "nama": "Kewarganegaraan", "sks": 1, "wajib": True},
                # Pilihan (16 SKS)
                {"kode": "TI109", "nama": "Statistika Dasar", "sks": 2, "wajib": False},
                {"kode": "TI110", "nama": "Kalkulus Dasar", "sks": 2, "wajib": False},
                {"kode": "TI111", "nama": "Pengantar Sistem Informasi", "sks": 2, "wajib": False},
                {"kode": "TI112", "nama": "Logika Digital", "sks": 2, "wajib": False},
                {"kode": "TI113", "nama": "Komunikasi Teknis", "sks": 1, "wajib": False},
                {"kode": "TI114", "nama": "Kepemimpinan Digital", "sks": 1, "wajib": False},
                {"kode": "TI115", "nama": "Literasi Data", "sks": 2, "wajib": False},
                {"kode": "TI116", "nama": "Pengantar Pemrograman Web", "sks": 2, "wajib": False},
                {"kode": "TI117", "nama": "Komputer & Masyarakat", "sks": 1, "wajib": False},
                {"kode": "TI118", "nama": "Praktikum Algoritma", "sks": 1, "wajib": False},
            ],
            2: [
                # Wajib (12 SKS)
                {"kode": "TI201", "nama": "Pemrograman Berorientasi Objek", "sks": 2, "wajib": True},
                {"kode": "TI202", "nama": "Basis Data Dasar", "sks": 2, "wajib": True},
                {"kode": "TI203", "nama": "Struktur Data", "sks": 2, "wajib": True},
                {"kode": "TI204", "nama": "Sistem Operasi", "sks": 2, "wajib": True},
                {"kode": "TI205", "nama": "Matematika Komputasi", "sks": 2, "wajib": True},
                {"kode": "TI206", "nama": "Bahasa Inggris II", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "TI207", "nama": "Pemrograman Fungsional", "sks": 2, "wajib": False},
                {"kode": "TI208", "nama": "Komunikasi Data", "sks": 2, "wajib": False},
                {"kode": "TI209", "nama": "Keamanan Informasi Dasar", "sks": 1, "wajib": False},
                {"kode": "TI210", "nama": "Grafika Komputer", "sks": 2, "wajib": False},
                {"kode": "TI211", "nama": "Desain Basis Data Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI212", "nama": "Algoritma Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI213", "nama": "Kewirausahaan Digital", "sks": 2, "wajib": False},
                {"kode": "TI214", "nama": "Pengujian Perangkat Lunak", "sks": 1, "wajib": False},
                {"kode": "TI215", "nama": "Praktikum Basis Data", "sks": 1, "wajib": False},
                {"kode": "TI216", "nama": "Basis Data NoSQL", "sks": 1, "wajib": False},
            ],
            3: [
                # Wajib (12 SKS)
                {"kode": "TI301", "nama": "Rekayasa Perangkat Lunak", "sks": 2, "wajib": True},
                {"kode": "TI302", "nama": "Jaringan Komputer", "sks": 2, "wajib": True},
                {"kode": "TI303", "nama": "Kecerdasan Buatan Dasar", "sks": 2, "wajib": True},
                {"kode": "TI304", "nama": "Analisis & Desain Sistem", "sks": 2, "wajib": True},
                {"kode": "TI305", "nama": "Pemrograman Web Front-end", "sks": 2, "wajib": True},
                {"kode": "TI306", "nama": "Pemrograman Web Back-end", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "TI307", "nama": "Keamanan Sistem Informasi", "sks": 1, "wajib": False},
                {"kode": "TI308", "nama": "Pemrograman Mobile", "sks": 2, "wajib": False},
                {"kode": "TI309", "nama": "Machine Learning Dasar", "sks": 2, "wajib": False},
                {"kode": "TI310", "nama": "DevOps Dasar", "sks": 2, "wajib": False},
                {"kode": "TI311", "nama": "Desain Antarmuka", "sks": 1, "wajib": False},
                {"kode": "TI312", "nama": "API Development", "sks": 2, "wajib": False},
                {"kode": "TI313", "nama": "Analisis Data", "sks": 2, "wajib": False},
                {"kode": "TI314", "nama": "Etika Profesi IT", "sks": 1, "wajib": False},
                {"kode": "TI315", "nama": "Bahasa Inggris III", "sks": 1, "wajib": False},
                {"kode": "TI316", "nama": "Sistem Tertanam", "sks": 1, "wajib": False},
                {"kode": "TI317", "nama": "Manajemen Konfigurasi", "sks": 1, "wajib": False},
                {"kode": "TI318", "nama": "Jaringan Nirkabel", "sks": 2, "wajib": False},
            ],
            4: [
                # Wajib (10 SKS)
                {"kode": "TI401", "nama": "Pengembangan Aplikasi Mobile", "sks": 2, "wajib": True},
                {"kode": "TI402", "nama": "Cloud Computing", "sks": 2, "wajib": True},
                {"kode": "TI403", "nama": "Data Mining", "sks": 2, "wajib": True},
                {"kode": "TI404", "nama": "Pemrograman Berbasis Komponen", "sks": 2, "wajib": True},
                {"kode": "TI405", "nama": "Manajemen Proyek TI", "sks": 2, "wajib": True},
                # Pilihan (30 matkul)
                {"kode": "TI406", "nama": "Interaksi Manusia Komputer", "sks": 1, "wajib": False},
                {"kode": "TI407", "nama": "Cloud Deployment", "sks": 2, "wajib": False},
                {"kode": "TI408", "nama": "Data Warehouse", "sks": 2, "wajib": False},
                {"kode": "TI409", "nama": "Arsitektur Microservices", "sks": 2, "wajib": False},
                {"kode": "TI410", "nama": "Pengujian Aplikasi", "sks": 1, "wajib": False},
                {"kode": "TI411", "nama": "Bahasa Inggris IV", "sks": 1, "wajib": False},
                {"kode": "TI412", "nama": "Machine Learning Terapan", "sks": 2, "wajib": False},
                {"kode": "TI413", "nama": "Keamanan Jaringan", "sks": 2, "wajib": False},
                {"kode": "TI414", "nama": "Blockchain & Web3", "sks": 1, "wajib": False},
                {"kode": "TI415", "nama": "Pemrograman Paralel", "sks": 2, "wajib": False},
                {"kode": "TI416", "nama": "Visualisasi Data", "sks": 1, "wajib": False},
                {"kode": "TI417", "nama": "Natural Language Processing", "sks": 2, "wajib": False},
                {"kode": "TI418", "nama": "Sistem Rekomendasi", "sks": 1, "wajib": False},
                {"kode": "TI419", "nama": "Pengembangan Game", "sks": 2, "wajib": False},
                {"kode": "TI420", "nama": "Komputasi Awan Hybrid", "sks": 2, "wajib": False},
                {"kode": "TI421", "nama": "Keamanan Aplikasi Web", "sks": 2, "wajib": False},
                {"kode": "TI422", "nama": "Analitik Bisnis", "sks": 2, "wajib": False},
                {"kode": "TI423", "nama": "Pemrograman IoT", "sks": 2, "wajib": False},
                {"kode": "TI424", "nama": "UI/UX Design", "sks": 2, "wajib": False},
                {"kode": "TI425", "nama": "Sistem Pakar", "sks": 2, "wajib": False},
                {"kode": "TI426", "nama": "Pemrosesan Bahasa Alami Dasar", "sks": 1, "wajib": False},
                {"kode": "TI427", "nama": "Robotika & Otomasi", "sks": 2, "wajib": False},
                {"kode": "TI428", "nama": "Etika Kecerdasan Buatan", "sks": 1, "wajib": False},
                {"kode": "TI429", "nama": "Pengembangan API RESTful", "sks": 2, "wajib": False},
                {"kode": "TI430", "nama": "Manajemen Layanan TI", "sks": 1, "wajib": False},
            ],
            5: [
                # Wajib (8 SKS)
                {"kode": "TI501", "nama": "Machine Learning Lanjut", "sks": 2, "wajib": True},
                {"kode": "TI502", "nama": "Sistem Terdistribusi", "sks": 2, "wajib": True},
                {"kode": "TI503", "nama": "Metodologi Penelitian", "sks": 2, "wajib": True},
                {"kode": "TI504", "nama": "Seminar Proposal TA", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "TI505", "nama": "IoT & Embedded Systems", "sks": 2, "wajib": False},
                {"kode": "TI506", "nama": "Business Intelligence", "sks": 2, "wajib": False},
                {"kode": "TI507", "nama": "Deep Learning", "sks": 2, "wajib": False},
                {"kode": "TI508", "nama": "Computer Vision", "sks": 1, "wajib": False},
                {"kode": "TI509", "nama": "Big Data Analytics", "sks": 2, "wajib": False},
                {"kode": "TI510", "nama": "Keamanan Siber Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI511", "nama": "Pengembangan Game", "sks": 1, "wajib": False},
                {"kode": "TI512", "nama": "Augmented Reality", "sks": 2, "wajib": False},
                {"kode": "TI513", "nama": "Komputasi Awan Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI514", "nama": "Fintech & Digital Payment", "sks": 1, "wajib": False},
                {"kode": "TI515", "nama": "E-Commerce Platform", "sks": 2, "wajib": False},
                {"kode": "TI516", "nama": "Sistem Informasi Enterprise", "sks": 1, "wajib": False},
                {"kode": "TI517", "nama": "Manajemen Proyek Lanjut", "sks": 2, "wajib": False},
            ],
            6: [
                # Wajib (6 SKS)
                {"kode": "TI601", "nama": "Tugas Akhir", "sks": 2, "wajib": True},
                {"kode": "TI602", "nama": "Kerja Praktik", "sks": 2, "wajib": True},
                {"kode": "TI603", "nama": "Seminar Hasil TA", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "TI604", "nama": "Deep Learning Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI605", "nama": "Analisis Big Data Lanjut", "sks": 2, "wajib": False},
                {"kode": "TI606", "nama": "Technopreneurship", "sks": 2, "wajib": False},
                {"kode": "TI607", "nama": "Pengembangan Startup", "sks": 2, "wajib": False},
                {"kode": "TI608", "nama": "Transformasi Digital", "sks": 2, "wajib": False},
                {"kode": "TI609", "nama": "Digital Marketing Teknologi", "sks": 2, "wajib": False},
                {"kode": "TI610", "nama": "Arsitektur Enterprise", "sks": 2, "wajib": False},
                {"kode": "TI611", "nama": "Hukum TI & HAKI", "sks": 1, "wajib": False},
                {"kode": "TI612", "nama": "Keamanan Cloud", "sks": 2, "wajib": False},
                {"kode": "TI613", "nama": "AI Ethics & Governance", "sks": 1, "wajib": False},
                {"kode": "TI614", "nama": "Penelitian Lanjut", "sks": 2, "wajib": False},
            ],
        },
    },
    "AK": {
        "name": "Akuntansi",
        "prodi_code": "025",
        "semesters": {
            1: [
                # Wajib (13 SKS)
                {"kode": "AK101", "nama": "Pengantar Akuntansi I", "sks": 2, "wajib": True},
                {"kode": "AK102", "nama": "Matematika Ekonomi", "sks": 2, "wajib": True},
                {"kode": "AK103", "nama": "Pengantar Bisnis", "sks": 2, "wajib": True},
                {"kode": "AK104", "nama": "Ekonomi Mikro", "sks": 2, "wajib": True},
                {"kode": "AK105", "nama": "Bahasa Indonesia", "sks": 1, "wajib": True},
                {"kode": "AK106", "nama": "Bahasa Inggris Bisnis I", "sks": 2, "wajib": True},
                {"kode": "AK107", "nama": "Pendidikan Agama & Moral", "sks": 2, "wajib": True},
                # Pilihan (17 SKS)
                {"kode": "AK108", "nama": "Kewarganegaraan", "sks": 1, "wajib": False},
                {"kode": "AK109", "nama": "Pengantar Manajemen", "sks": 2, "wajib": False},
                {"kode": "AK110", "nama": "Statistika Bisnis", "sks": 2, "wajib": False},
                {"kode": "AK111", "nama": "Komunikasi Bisnis", "sks": 2, "wajib": False},
                {"kode": "AK112", "nama": "Etika Bisnis", "sks": 1, "wajib": False},
                {"kode": "AK113", "nama": "Teknologi Informasi Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK114", "nama": "Pengantar Perpajakan", "sks": 2, "wajib": False},
                {"kode": "AK115", "nama": "Matematika Keuangan", "sks": 2, "wajib": False},
                {"kode": "AK116", "nama": "Pengantar Hukum Bisnis", "sks": 1, "wajib": False},
                {"kode": "AK117", "nama": "Kepemimpinan Organisasi", "sks": 1, "wajib": False},
                {"kode": "AK118", "nama": "Bahasa Inggris Bisnis II", "sks": 1, "wajib": False},
            ],
            2: [
                # Wajib (12 SKS)
                {"kode": "AK201", "nama": "Pengantar Akuntansi II", "sks": 2, "wajib": True},
                {"kode": "AK202", "nama": "Akuntansi Keuangan Menengah I", "sks": 2, "wajib": True},
                {"kode": "AK203", "nama": "Ekonomi Makro", "sks": 2, "wajib": True},
                {"kode": "AK204", "nama": "Hukum Bisnis", "sks": 2, "wajib": True},
                {"kode": "AK205", "nama": "Statistika Bisnis Lanjut", "sks": 2, "wajib": True},
                {"kode": "AK206", "nama": "Komputer Akuntansi", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "AK207", "nama": "Bahasa Inggris Bisnis III", "sks": 1, "wajib": False},
                {"kode": "AK208", "nama": "Akuntansi Kos I", "sks": 2, "wajib": False},
                {"kode": "AK209", "nama": "Sistem Informasi Akuntansi Dasar", "sks": 2, "wajib": False},
                {"kode": "AK210", "nama": "Pengantar Auditing", "sks": 1, "wajib": False},
                {"kode": "AK211", "nama": "Analisis Investasi Dasar", "sks": 2, "wajib": False},
                {"kode": "AK212", "nama": "Kewirausahaan Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK213", "nama": "Manajemen Keuangan Dasar", "sks": 2, "wajib": False},
                {"kode": "AK214", "nama": "Akuntansi Pemerintah Dasar", "sks": 1, "wajib": False},
                {"kode": "AK215", "nama": "Pelaporan Keuangan Digital", "sks": 2, "wajib": False},
                {"kode": "AK216", "nama": "Komunikasi Laporan Keuangan", "sks": 1, "wajib": False},
            ],
            3: [
                # Wajib (12 SKS)
                {"kode": "AK301", "nama": "Akuntansi Keuangan Menengah II", "sks": 2, "wajib": True},
                {"kode": "AK302", "nama": "Akuntansi Biaya", "sks": 2, "wajib": True},
                {"kode": "AK303", "nama": "Akuntansi Manajemen", "sks": 2, "wajib": True},
                {"kode": "AK304", "nama": "Perpajakan I", "sks": 2, "wajib": True},
                {"kode": "AK305", "nama": "Sistem Informasi Akuntansi", "sks": 2, "wajib": True},
                {"kode": "AK306", "nama": "Auditing I", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "AK307", "nama": "Kewirausahaan Lanjut", "sks": 1, "wajib": False},
                {"kode": "AK308", "nama": "Analisis Laporan Keuangan Dasar", "sks": 2, "wajib": False},
                {"kode": "AK309", "nama": "Akuntansi Biaya Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK310", "nama": "Manajemen Pajak", "sks": 1, "wajib": False},
                {"kode": "AK311", "nama": "Audit Internal", "sks": 2, "wajib": False},
                {"kode": "AK312", "nama": "Akuntansi Digital", "sks": 2, "wajib": False},
                {"kode": "AK313", "nama": "Data Analytics Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK314", "nama": "Etika Profesi Akuntansi", "sks": 1, "wajib": False},
                {"kode": "AK315", "nama": "Bahasa Inggris Akuntansi", "sks": 1, "wajib": False},
                {"kode": "AK316", "nama": "Hukum Pajak", "sks": 2, "wajib": False},
                {"kode": "AK317", "nama": "Pelaporan CSR", "sks": 2, "wajib": False},
            ],
            4: [
                # Wajib (10 SKS)
                {"kode": "AK401", "nama": "Akuntansi Keuangan Lanjutan I", "sks": 2, "wajib": True},
                {"kode": "AK402", "nama": "Akuntansi Sektor Publik", "sks": 2, "wajib": True},
                {"kode": "AK403", "nama": "Perpajakan II", "sks": 2, "wajib": True},
                {"kode": "AK404", "nama": "Auditing II", "sks": 2, "wajib": True},
                {"kode": "AK405", "nama": "Manajemen Keuangan", "sks": 2, "wajib": True},
                # Pilihan (30 matkul)
                {"kode": "AK406", "nama": "Analisis Laporan Keuangan", "sks": 2, "wajib": False},
                {"kode": "AK407", "nama": "Bahasa Inggris IV", "sks": 1, "wajib": False},
                {"kode": "AK408", "nama": "Akuntansi Kontrak Konstruksi", "sks": 2, "wajib": False},
                {"kode": "AK409", "nama": "Manajemen Risiko Keuangan", "sks": 2, "wajib": False},
                {"kode": "AK410", "nama": "Akuntansi Forensik Dasar", "sks": 1, "wajib": False},
                {"kode": "AK411", "nama": "Pasar Modal Dasar", "sks": 2, "wajib": False},
                {"kode": "AK412", "nama": "Akuntansi Lingkungan", "sks": 1, "wajib": False},
                {"kode": "AK413", "nama": "Akuntansi Internasional", "sks": 2, "wajib": False},
                {"kode": "AK414", "nama": "Manajemen Aset", "sks": 2, "wajib": False},
                {"kode": "AK415", "nama": "Perpajakan Internasional", "sks": 1, "wajib": False},
                {"kode": "AK416", "nama": "Digital Banking", "sks": 2, "wajib": False},
                {"kode": "AK417", "nama": "Analisis Biaya-Manfaat", "sks": 1, "wajib": False},
                {"kode": "AK418", "nama": "Akuntansi Syariah Dasar", "sks": 2, "wajib": False},
                {"kode": "AK419", "nama": "Penganggaran Perusahaan", "sks": 2, "wajib": False},
                {"kode": "AK420", "nama": "Audit Sistem Informasi", "sks": 2, "wajib": False},
                {"kode": "AK421", "nama": "Akuntansi Perbankan", "sks": 2, "wajib": False},
                {"kode": "AK422", "nama": "Perencanaan Pajak", "sks": 2, "wajib": False},
                {"kode": "AK423", "nama": "Manajemen Investasi", "sks": 2, "wajib": False},
                {"kode": "AK424", "nama": "Akuntansi Biaya Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK425", "nama": "Sistem Pengendalian Manajemen", "sks": 2, "wajib": False},
                {"kode": "AK426", "nama": "Etika Bisnis & Profesi", "sks": 1, "wajib": False},
                {"kode": "AK427", "nama": "Kewirausahaan Berbasis Akuntansi", "sks": 1, "wajib": False},
                {"kode": "AK428", "nama": "Analitik Data Keuangan", "sks": 2, "wajib": False},
                {"kode": "AK429", "nama": "Pelaporan Keberlanjutan", "sks": 1, "wajib": False},
                {"kode": "AK430", "nama": "Manajemen Kas & Treasury", "sks": 2, "wajib": False},
            ],
            5: [
                # Wajib (8 SKS)
                {"kode": "AK501", "nama": "Akuntansi Keuangan Lanjutan II", "sks": 2, "wajib": True},
                {"kode": "AK502", "nama": "Teori Akuntansi", "sks": 2, "wajib": True},
                {"kode": "AK503", "nama": "Metodologi Penelitian Akuntansi", "sks": 2, "wajib": True},
                {"kode": "AK504", "nama": "Seminar Akuntansi", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "AK505", "nama": "Akuntansi Syariah", "sks": 2, "wajib": False},
                {"kode": "AK506", "nama": "Pasar Modal & Investasi", "sks": 2, "wajib": False},
                {"kode": "AK507", "nama": "Akuntansi Forensik Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK508", "nama": "Akuntansi Sosial & Lingkungan", "sks": 1, "wajib": False},
                {"kode": "AK509", "nama": "Manajemen Keuangan Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK510", "nama": "Audit Berbasis Risiko", "sks": 2, "wajib": False},
                {"kode": "AK511", "nama": "Tata Kelola Perusahaan", "sks": 2, "wajib": False},
                {"kode": "AK512", "nama": "Pelaporan Terintegrasi", "sks": 1, "wajib": False},
                {"kode": "AK513", "nama": "Big Data Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK514", "nama": "Blockchain Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK515", "nama": "Akuntansi Startup", "sks": 1, "wajib": False},
                {"kode": "AK516", "nama": "Valuasi Bisnis", "sks": 1, "wajib": False},
                {"kode": "AK517", "nama": "Literasi Keuangan Digital", "sks": 2, "wajib": False},
            ],
            6: [
                # Wajib (6 SKS)
                {"kode": "AK601", "nama": "Tugas Akhir/Skripsi", "sks": 2, "wajib": True},
                {"kode": "AK602", "nama": "Magang Profesi", "sks": 2, "wajib": True},
                {"kode": "AK603", "nama": "Seminar Hasil", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "AK604", "nama": "Akuntansi Lingkungan Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK605", "nama": "Tata Kelola Perusahaan Lanjut", "sks": 2, "wajib": False},
                {"kode": "AK606", "nama": "Etika Profesi Akuntan", "sks": 1, "wajib": False},
                {"kode": "AK607", "nama": "Seminar Perpajakan", "sks": 1, "wajib": False},
                {"kode": "AK608", "nama": "Manajemen Keuangan Digital", "sks": 2, "wajib": False},
                {"kode": "AK609", "nama": "Fintech & Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AK610", "nama": "Audit Digital", "sks": 2, "wajib": False},
                {"kode": "AK611", "nama": "Akuntansi Global", "sks": 2, "wajib": False},
                {"kode": "AK612", "nama": "Pelaporan Keuangan IFRS", "sks": 2, "wajib": False},
                {"kode": "AK613", "nama": "Analisis Portofolio", "sks": 2, "wajib": False},
                {"kode": "AK614", "nama": "Kewirausahaan Berbasis Data", "sks": 2, "wajib": False},
            ],
        },
    },
    "TM": {
        "name": "Teknik Mesin",
        "prodi_code": "026",
        "semesters": {
            1: [
                # Wajib (14 SKS)
                {"kode": "TM101", "nama": "Matematika Teknik I", "sks": 2, "wajib": True},
                {"kode": "TM102", "nama": "Fisika Teknik I", "sks": 2, "wajib": True},
                {"kode": "TM103", "nama": "Menggambar Teknik", "sks": 2, "wajib": True},
                {"kode": "TM104", "nama": "Kimia Teknik", "sks": 2, "wajib": True},
                {"kode": "TM105", "nama": "Bahasa Indonesia", "sks": 1, "wajib": True},
                {"kode": "TM106", "nama": "Bahasa Inggris Teknik I", "sks": 2, "wajib": True},
                {"kode": "TM107", "nama": "Pendidikan Agama", "sks": 2, "wajib": True},
                {"kode": "TM108", "nama": "Kewarganegaraan", "sks": 1, "wajib": True},
                # Pilihan (16 SKS)
                {"kode": "TM109", "nama": "Kalkulus I", "sks": 2, "wajib": False},
                {"kode": "TM110", "nama": "Pengantar Teknik Mesin", "sks": 2, "wajib": False},
                {"kode": "TM111", "nama": "Praktikum Menggambar", "sks": 1, "wajib": False},
                {"kode": "TM112", "nama": "Mekanika Vektor", "sks": 2, "wajib": False},
                {"kode": "TM113", "nama": "Logika Berpikir Teknik", "sks": 1, "wajib": False},
                {"kode": "TM114", "nama": "Pengantar Material", "sks": 2, "wajib": False},
                {"kode": "TM115", "nama": "Laboratorium Fisika", "sks": 1, "wajib": False},
                {"kode": "TM116", "nama": "Teknologi Manufaktur Dasar", "sks": 2, "wajib": False},
                {"kode": "TM117", "nama": "Komunikasi Teknik", "sks": 1, "wajib": False},
                {"kode": "TM118", "nama": "Kewirausahaan Teknik Dasar", "sks": 2, "wajib": False},
            ],
            2: [
                # Wajib (12 SKS)
                {"kode": "TM201", "nama": "Matematika Teknik II", "sks": 2, "wajib": True},
                {"kode": "TM202", "nama": "Fisika Teknik II", "sks": 2, "wajib": True},
                {"kode": "TM203", "nama": "Mekanika Teknik", "sks": 2, "wajib": True},
                {"kode": "TM204", "nama": "Material Teknik", "sks": 2, "wajib": True},
                {"kode": "TM205", "nama": "Termodinamika I", "sks": 2, "wajib": True},
                {"kode": "TM206", "nama": "Statistika Teknik", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "TM207", "nama": "Bahasa Inggris Teknik II", "sks": 1, "wajib": False},
                {"kode": "TM208", "nama": "Kalkulus II", "sks": 2, "wajib": False},
                {"kode": "TM209", "nama": "Menggambar Mesin", "sks": 2, "wajib": False},
                {"kode": "TM210", "nama": "Pengantar Elemen Mesin", "sks": 2, "wajib": False},
                {"kode": "TM211", "nama": "Mekanika Kekuatan Material", "sks": 2, "wajib": False},
                {"kode": "TM212", "nama": "Praktikum Material", "sks": 1, "wajib": False},
                {"kode": "TM213", "nama": "Pengantar Mekanika Fluida", "sks": 2, "wajib": False},
                {"kode": "TM214", "nama": "CAD Dasar", "sks": 2, "wajib": False},
                {"kode": "TM215", "nama": "Pengukuran Teknik", "sks": 1, "wajib": False},
                {"kode": "TM216", "nama": "Kewirausahaan Teknik", "sks": 1, "wajib": False},
            ],
            3: [
                # Wajib (12 SKS)
                {"kode": "TM301", "nama": "Mekanika Fluida", "sks": 2, "wajib": True},
                {"kode": "TM302", "nama": "Elemen Mesin I", "sks": 2, "wajib": True},
                {"kode": "TM303", "nama": "Termodinamika II", "sks": 2, "wajib": True},
                {"kode": "TM304", "nama": "Proses Manufaktur", "sks": 2, "wajib": True},
                {"kode": "TM305", "nama": "Perpindahan Panas I", "sks": 2, "wajib": True},
                {"kode": "TM306", "nama": "Kinematika & Dinamika", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "TM307", "nama": "Gambar Mesin CAD", "sks": 2, "wajib": False},
                {"kode": "TM308", "nama": "Elemen Mesin Terapan", "sks": 1, "wajib": False},
                {"kode": "TM309", "nama": "Metalurgi Dasar", "sks": 2, "wajib": False},
                {"kode": "TM310", "nama": "Getaran Mekanik Dasar", "sks": 1, "wajib": False},
                {"kode": "TM311", "nama": "Bahasa Inggris Teknik III", "sks": 1, "wajib": False},
                {"kode": "TM312", "nama": "Teknologi Las Dasar", "sks": 2, "wajib": False},
                {"kode": "TM313", "nama": "Pengantar Kontrol", "sks": 1, "wajib": False},
                {"kode": "TM314", "nama": "Mekanika Fluida Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM315", "nama": "Material Komposit", "sks": 2, "wajib": False},
                {"kode": "TM316", "nama": "Analisis Numerik", "sks": 2, "wajib": False},
                {"kode": "TM317", "nama": "Praktikum Manufaktur", "sks": 1, "wajib": False},
                {"kode": "TM318", "nama": "Teknik Lingkungan Dasar", "sks": 1, "wajib": False},
            ],
            4: [
                # Wajib (10 SKS)
                {"kode": "TM401", "nama": "Elemen Mesin II", "sks": 2, "wajib": True},
                {"kode": "TM402", "nama": "Perpindahan Panas II", "sks": 2, "wajib": True},
                {"kode": "TM403", "nama": "Mesin-mesin Fluida", "sks": 2, "wajib": True},
                {"kode": "TM404", "nama": "Pengendalian Proses", "sks": 2, "wajib": True},
                {"kode": "TM405", "nama": "Teknik Pengelasan", "sks": 2, "wajib": True},
                # Pilihan (30 matkul)
                {"kode": "TM406", "nama": "Getaran Mekanik", "sks": 2, "wajib": False},
                {"kode": "TM407", "nama": "Pneumatik & Hidrolik", "sks": 2, "wajib": False},
                {"kode": "TM408", "nama": "Perancangan Mesin Dasar", "sks": 2, "wajib": False},
                {"kode": "TM409", "nama": "Otomasi Industri Dasar", "sks": 1, "wajib": False},
                {"kode": "TM410", "nama": "Analisis Kegagalan Material", "sks": 2, "wajib": False},
                {"kode": "TM411", "nama": "Teknik Permesinan CNC", "sks": 2, "wajib": False},
                {"kode": "TM412", "nama": "Sistem Kontrol Lanjut", "sks": 1, "wajib": False},
                {"kode": "TM413", "nama": "Simulasi Teknik", "sks": 2, "wajib": False},
                {"kode": "TM414", "nama": "Manajemen Produksi", "sks": 1, "wajib": False},
                {"kode": "TM415", "nama": "Bahasa Inggris Teknik IV", "sks": 1, "wajib": False},
                {"kode": "TM416", "nama": "Thermofluida Terapan", "sks": 2, "wajib": False},
                {"kode": "TM417", "nama": "Teknik Pendingin Dasar", "sks": 1, "wajib": False},
                {"kode": "TM418", "nama": "Ergonomi Industri", "sks": 1, "wajib": False},
                {"kode": "TM419", "nama": "Teknik Korosi & Proteksi", "sks": 2, "wajib": False},
                {"kode": "TM420", "nama": "Mekatronika Dasar", "sks": 2, "wajib": False},
                {"kode": "TM421", "nama": "Analisis Tegangan", "sks": 2, "wajib": False},
                {"kode": "TM422", "nama": "Teknologi Pengelasan Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM423", "nama": "Sistem Propulsi", "sks": 2, "wajib": False},
                {"kode": "TM424", "nama": "Manajemen Energi Industri", "sks": 2, "wajib": False},
                {"kode": "TM425", "nama": "Teknik Pengecoran", "sks": 2, "wajib": False},
                {"kode": "TM426", "nama": "Pemodelan & Simulasi CAD", "sks": 2, "wajib": False},
                {"kode": "TM427", "nama": "Kewirausahaan Teknik Mesin", "sks": 1, "wajib": False},
                {"kode": "TM428", "nama": "Teknik Keselamatan Industri", "sks": 1, "wajib": False},
                {"kode": "TM429", "nama": "Metalurgi Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM430", "nama": "Sistem Manufaktur Fleksibel", "sks": 2, "wajib": False},
            ],
            5: [
                # Wajib (8 SKS)
                {"kode": "TM501", "nama": "Perancangan Mesin", "sks": 2, "wajib": True},
                {"kode": "TM502", "nama": "Sistem Pembangkit Tenaga", "sks": 2, "wajib": True},
                {"kode": "TM503", "nama": "Metodologi Penelitian", "sks": 2, "wajib": True},
                {"kode": "TM504", "nama": "Seminar Proposal TA", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "TM505", "nama": "Tribologi & Pelumasan", "sks": 2, "wajib": False},
                {"kode": "TM506", "nama": "Teknik Pendingin & AC", "sks": 2, "wajib": False},
                {"kode": "TM507", "nama": "Komputasi Numerik", "sks": 2, "wajib": False},
                {"kode": "TM508", "nama": "Otomasi Industri Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM509", "nama": "Energi Terbarukan", "sks": 2, "wajib": False},
                {"kode": "TM510", "nama": "Mesin Konversi Energi", "sks": 2, "wajib": False},
                {"kode": "TM511", "nama": "Manufaktur Lanjut", "sks": 1, "wajib": False},
                {"kode": "TM512", "nama": "Material Nano", "sks": 1, "wajib": False},
                {"kode": "TM513", "nama": "Teknik Pendingin Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM514", "nama": "Dinamika Mesin", "sks": 2, "wajib": False},
                {"kode": "TM515", "nama": "Kewirausahaan Manufaktur", "sks": 1, "wajib": False},
                {"kode": "TM516", "nama": "Teknik Keselamatan", "sks": 1, "wajib": False},
                {"kode": "TM517", "nama": "Manajemen Energi", "sks": 2, "wajib": False},
            ],
            6: [
                # Wajib (6 SKS)
                {"kode": "TM601", "nama": "Tugas Akhir", "sks": 2, "wajib": True},
                {"kode": "TM602", "nama": "Kerja Praktik", "sks": 2, "wajib": True},
                {"kode": "TM603", "nama": "Seminar Hasil TA", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "TM604", "nama": "Otomasi Industri Terapan", "sks": 2, "wajib": False},
                {"kode": "TM605", "nama": "Manajemen Industri", "sks": 2, "wajib": False},
                {"kode": "TM606", "nama": "Energi Terbarukan Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM607", "nama": "Kewirausahaan Teknik", "sks": 2, "wajib": False},
                {"kode": "TM608", "nama": "Sistem Produksi Lean", "sks": 2, "wajib": False},
                {"kode": "TM609", "nama": "Teknik Keselamatan Kerja", "sks": 1, "wajib": False},
                {"kode": "TM610", "nama": "Manajemen Perawatan", "sks": 2, "wajib": False},
                {"kode": "TM611", "nama": "Hukum Industri", "sks": 1, "wajib": False},
                {"kode": "TM612", "nama": "Perancangan Produk", "sks": 2, "wajib": False},
                {"kode": "TM613", "nama": "Analisis Getaran Lanjut", "sks": 2, "wajib": False},
                {"kode": "TM614", "nama": "Robotika Industri", "sks": 2, "wajib": False},
            ],
        },
    },
    "AP": {
        "name": "Administrasi Perkantoran",
        "prodi_code": "027",
        "semesters": {
            1: [
                # Wajib (12 SKS)
                {"kode": "AP101", "nama": "Pengantar Administrasi Perkantoran", "sks": 2, "wajib": True},
                {"kode": "AP102", "nama": "Komunikasi Bisnis", "sks": 2, "wajib": True},
                {"kode": "AP103", "nama": "Komputer Perkantoran I", "sks": 2, "wajib": True},
                {"kode": "AP104", "nama": "Pengantar Manajemen", "sks": 1, "wajib": True},
                {"kode": "AP105", "nama": "Bahasa Indonesia", "sks": 2, "wajib": True},
                {"kode": "AP106", "nama": "Bahasa Inggris Perkantoran I", "sks": 2, "wajib": True},
                {"kode": "AP107", "nama": "Pendidikan Agama & Moral", "sks": 1, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "AP108", "nama": "Kewarganegaraan", "sks": 1, "wajib": False},
                {"kode": "AP109", "nama": "Matematika Bisnis", "sks": 2, "wajib": False},
                {"kode": "AP110", "nama": "Pengetikan Profesional", "sks": 1, "wajib": False},
                {"kode": "AP111", "nama": "Etika Perkantoran", "sks": 1, "wajib": False},
                {"kode": "AP112", "nama": "Komunikasi Interpersonal", "sks": 2, "wajib": False},
                {"kode": "AP113", "nama": "Pengantar Akuntansi", "sks": 2, "wajib": False},
                {"kode": "AP114", "nama": "Teknologi Informasi Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP115", "nama": "Kepemimpinan Dasar", "sks": 1, "wajib": False},
                {"kode": "AP116", "nama": "Manajemen Waktu & Produktivitas", "sks": 2, "wajib": False},
                {"kode": "AP117", "nama": "Bahasa Inggris Bisnis I", "sks": 2, "wajib": False},
                {"kode": "AP118", "nama": "Public Speaking Dasar", "sks": 2, "wajib": False},
            ],
            2: [
                # Wajib (12 SKS)
                {"kode": "AP201", "nama": "Manajemen Kearsipan", "sks": 2, "wajib": True},
                {"kode": "AP202", "nama": "Komputer Perkantoran II", "sks": 2, "wajib": True},
                {"kode": "AP203", "nama": "Korespondensi Bisnis", "sks": 2, "wajib": True},
                {"kode": "AP204", "nama": "Tata Kelola Perkantoran", "sks": 2, "wajib": True},
                {"kode": "AP205", "nama": "Kesekretarisan", "sks": 2, "wajib": True},
                {"kode": "AP206", "nama": "Ekonomi & Bisnis", "sks": 2, "wajib": True},
                # Pilihan (17 SKS)
                {"kode": "AP207", "nama": "Bahasa Inggris Perkantoran II", "sks": 1, "wajib": False},
                {"kode": "AP208", "nama": "Hukum Perkantoran", "sks": 1, "wajib": False},
                {"kode": "AP209", "nama": "Manajemen Dokumen Digital", "sks": 2, "wajib": False},
                {"kode": "AP210", "nama": "Pelayanan Prima", "sks": 2, "wajib": False},
                {"kode": "AP211", "nama": "Administrasi Kepegawaian Dasar", "sks": 2, "wajib": False},
                {"kode": "AP212", "nama": "Komunikasi Organisasi", "sks": 2, "wajib": False},
                {"kode": "AP213", "nama": "Manajemen Rapat", "sks": 1, "wajib": False},
                {"kode": "AP214", "nama": "Kewirausahaan Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP215", "nama": "Pengantar E-Office", "sks": 1, "wajib": False},
                {"kode": "AP216", "nama": "Psikologi Kerja", "sks": 2, "wajib": False},
                {"kode": "AP217", "nama": "Protokoler Dasar", "sks": 1, "wajib": False},
            ],
            3: [
                # Wajib (12 SKS)
                {"kode": "AP301", "nama": "Manajemen Sumber Daya Manusia", "sks": 2, "wajib": True},
                {"kode": "AP302", "nama": "Sistem Informasi Manajemen", "sks": 2, "wajib": True},
                {"kode": "AP303", "nama": "Public Relations", "sks": 2, "wajib": True},
                {"kode": "AP304", "nama": "Manajemen Rapat & Protokoler", "sks": 2, "wajib": True},
                {"kode": "AP305", "nama": "Akuntansi Perkantoran", "sks": 2, "wajib": True},
                {"kode": "AP306", "nama": "Administrasi Kepegawaian", "sks": 2, "wajib": True},
                # Pilihan (18 SKS)
                {"kode": "AP307", "nama": "Kewirausahaan Perkantoran Lanjut", "sks": 1, "wajib": False},
                {"kode": "AP308", "nama": "Bahasa Inggris Perkantoran III", "sks": 2, "wajib": False},
                {"kode": "AP309", "nama": "Manajemen Konflik", "sks": 2, "wajib": False},
                {"kode": "AP310", "nama": "Negosiasi Bisnis", "sks": 2, "wajib": False},
                {"kode": "AP311", "nama": "Humas Internal", "sks": 1, "wajib": False},
                {"kode": "AP312", "nama": "Pengelolaan Aset Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP313", "nama": "Bahasa Mandarin Bisnis I", "sks": 2, "wajib": False},
                {"kode": "AP314", "nama": "Event Planning Dasar", "sks": 2, "wajib": False},
                {"kode": "AP315", "nama": "Komunikasi Krisis", "sks": 1, "wajib": False},
                {"kode": "AP316", "nama": "Layanan Pelanggan Digital", "sks": 2, "wajib": False},
                {"kode": "AP317", "nama": "Perkantoran Virtual", "sks": 1, "wajib": False},
            ],
            4: [
                # Wajib (10 SKS)
                {"kode": "AP401", "nama": "Manajemen Keuangan Perkantoran", "sks": 2, "wajib": True},
                {"kode": "AP402", "nama": "E-Office & Digitalisasi", "sks": 2, "wajib": True},
                {"kode": "AP403", "nama": "Humas & Protokol", "sks": 2, "wajib": True},
                {"kode": "AP404", "nama": "Manajemen Layanan Pelanggan", "sks": 2, "wajib": True},
                {"kode": "AP405", "nama": "Sistem Penggajian", "sks": 2, "wajib": True},
                # Pilihan (30 matkul)
                {"kode": "AP406", "nama": "Pengembangan Organisasi", "sks": 2, "wajib": False},
                {"kode": "AP407", "nama": "Presentasi Bisnis", "sks": 1, "wajib": False},
                {"kode": "AP408", "nama": "Bahasa Mandarin Bisnis II", "sks": 2, "wajib": False},
                {"kode": "AP409", "nama": "Manajemen Perubahan", "sks": 2, "wajib": False},
                {"kode": "AP410", "nama": "Komunikasi Antar Budaya", "sks": 1, "wajib": False},
                {"kode": "AP411", "nama": "Perencanaan SDM", "sks": 2, "wajib": False},
                {"kode": "AP412", "nama": "Digitalisasi Dokumen", "sks": 1, "wajib": False},
                {"kode": "AP413", "nama": "Manajemen Proyek Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP414", "nama": "Hukum Ketenagakerjaan", "sks": 2, "wajib": False},
                {"kode": "AP415", "nama": "Bahasa Inggris Perkantoran IV", "sks": 1, "wajib": False},
                {"kode": "AP416", "nama": "Analisis Jabatan", "sks": 2, "wajib": False},
                {"kode": "AP417", "nama": "Etika Digital", "sks": 1, "wajib": False},
                {"kode": "AP418", "nama": "Manajemen Rekrutmen", "sks": 2, "wajib": False},
                {"kode": "AP419", "nama": "Sistem Informasi Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP420", "nama": "Komunikasi Korporat", "sks": 2, "wajib": False},
                {"kode": "AP421", "nama": "Manajemen Arsip Digital", "sks": 2, "wajib": False},
                {"kode": "AP422", "nama": "Pelatihan & Pengembangan SDM", "sks": 2, "wajib": False},
                {"kode": "AP423", "nama": "Tata Kelola Perusahaan", "sks": 2, "wajib": False},
                {"kode": "AP424", "nama": "Manajemen Konflik Lanjut", "sks": 1, "wajib": False},
                {"kode": "AP425", "nama": "Kepemimpinan Transformasional", "sks": 2, "wajib": False},
                {"kode": "AP426", "nama": "Negosiasi & Mediasi", "sks": 2, "wajib": False},
                {"kode": "AP427", "nama": "Kewirausahaan Sosial", "sks": 1, "wajib": False},
                {"kode": "AP428", "nama": "Manajemen Event Korporat", "sks": 2, "wajib": False},
                {"kode": "AP429", "nama": "Psikologi Organisasi", "sks": 2, "wajib": False},
                {"kode": "AP430", "nama": "Administrasi Bisnis Digital", "sks": 2, "wajib": False},
            ],
            5: [
                # Wajib (8 SKS)
                {"kode": "AP501", "nama": "Manajemen Perkantoran Modern", "sks": 2, "wajib": True},
                {"kode": "AP502", "nama": "Metodologi Penelitian", "sks": 2, "wajib": True},
                {"kode": "AP503", "nama": "Seminar Administrasi", "sks": 2, "wajib": True},
                {"kode": "AP504", "nama": "Magang I", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "AP505", "nama": "Event Organizer & Manajemen Acara", "sks": 2, "wajib": False},
                {"kode": "AP506", "nama": "Bisnis Digital", "sks": 2, "wajib": False},
                {"kode": "AP507", "nama": "Perilaku Organisasi", "sks": 2, "wajib": False},
                {"kode": "AP508", "nama": "Leadership & Manajemen Tim", "sks": 2, "wajib": False},
                {"kode": "AP509", "nama": "Komunikasi Krisis Lanjut", "sks": 1, "wajib": False},
                {"kode": "AP510", "nama": "Teknologi SDM", "sks": 2, "wajib": False},
                {"kode": "AP511", "nama": "Manajemen Talenta", "sks": 2, "wajib": False},
                {"kode": "AP512", "nama": "Perkantoran Cerdas", "sks": 1, "wajib": False},
                {"kode": "AP513", "nama": "Strategi Layanan", "sks": 2, "wajib": False},
                {"kode": "AP514", "nama": "Administrasi Kontrak", "sks": 2, "wajib": False},
                {"kode": "AP515", "nama": "Manajemen Kinerja", "sks": 1, "wajib": False},
                {"kode": "AP516", "nama": "Kewirausahaan Digital", "sks": 1, "wajib": False},
                {"kode": "AP517", "nama": "Komunikasi Strategis", "sks": 2, "wajib": False},
            ],
            6: [
                # Wajib (6 SKS)
                {"kode": "AP601", "nama": "Tugas Akhir/Skripsi", "sks": 2, "wajib": True},
                {"kode": "AP602", "nama": "Magang Profesional", "sks": 2, "wajib": True},
                {"kode": "AP603", "nama": "Seminar Profesi", "sks": 2, "wajib": True},
                # Pilihan (22 SKS)
                {"kode": "AP604", "nama": "Manajemen Strategik", "sks": 2, "wajib": False},
                {"kode": "AP605", "nama": "Etika Profesi", "sks": 2, "wajib": False},
                {"kode": "AP606", "nama": "Kewirausahaan Lanjut", "sks": 2, "wajib": False},
                {"kode": "AP607", "nama": "Komunikasi Antar Budaya Lanjut", "sks": 2, "wajib": False},
                {"kode": "AP608", "nama": "Manajemen Inovasi", "sks": 2, "wajib": False},
                {"kode": "AP609", "nama": "Digital Transformation", "sks": 2, "wajib": False},
                {"kode": "AP610", "nama": "Pengembangan Karir", "sks": 1, "wajib": False},
                {"kode": "AP611", "nama": "Manajemen Risiko Perkantoran", "sks": 2, "wajib": False},
                {"kode": "AP612", "nama": "Kepemimpinan Eksekutif", "sks": 2, "wajib": False},
                {"kode": "AP613", "nama": "Business Process Improvement", "sks": 2, "wajib": False},
                {"kode": "AP614", "nama": "Hukum Administrasi", "sks": 1, "wajib": False},
            ],
        },
    },
}

PRODI_CODE_MAP = {
    "024": "TI",
    "025": "AK",
    "026": "TM",
    "027": "AP",
}


def get_prodi_key(nim: str) -> str:
    """Extract prodi key from NIM."""
    prodi_code = nim[2:5]
    return PRODI_CODE_MAP.get(prodi_code, "TI")


def get_wajib_courses(prodi_key: str, semester: int) -> list:
    """Get all mandatory courses for a given semester."""
    courses = CURRICULUM[prodi_key]["semesters"].get(semester, [])
    return [c for c in courses if c.get("wajib", False)]


def get_pilihan_courses(prodi_key: str, semester: int) -> list:
    """Get all elective courses for a given semester."""
    courses = CURRICULUM[prodi_key]["semesters"].get(semester, [])
    return [c for c in courses if not c.get("wajib", False)]


def get_semester_sks(prodi_key: str, semester: int) -> int:
    """Get total SKS for a given semester (all courses in pool)."""
    courses = CURRICULUM[prodi_key]["semesters"].get(semester, [])
    return sum(c["sks"] for c in courses)


def get_wajib_sks(prodi_key: str, semester: int) -> int:
    """Get total SKS for wajib courses in a semester."""
    return sum(c["sks"] for c in get_wajib_courses(prodi_key, semester))


def get_cumulative_sks(prodi_key: str, up_to_semester: int, sks_per_sem: dict = None) -> int:
    """Get cumulative SKS up to and including a semester."""
    total = 0
    for s in range(1, up_to_semester + 1):
        if sks_per_sem and s in sks_per_sem:
            total += sks_per_sem[s]
        else:
            # Default: wajib + enough electives to reach ~22 SKS
            w_sks = get_wajib_sks(prodi_key, s)
            total += max(w_sks, 22)
    return total


# Prerequisite mapping: {course_code: [list of prerequisite course codes]}
PREREQUISITES = {
    # TI Prerequisites
    "TI201": ["TI102"],  # PBO requires Algoritma Dasar
    "TI202": ["TI102"],  # Basis Data requires Algoritma Dasar
    "TI203": ["TI102"],  # Struktur Data requires Algoritma Dasar
    "TI212": ["TI203"],  # Algoritma Lanjut requires Struktur Data
    "TI301": ["TI201"],  # RPL requires PBO
    "TI303": ["TI203"],  # AI Dasar requires Struktur Data
    "TI305": ["TI201"],  # Web Front-end requires PBO
    "TI306": ["TI201", "TI202"],  # Web Back-end requires PBO & Basis Data
    "TI309": ["TI303"],  # ML Dasar requires AI Dasar
    "TI401": ["TI305"],  # Mobile requires Web Front-end
    "TI403": ["TI202"],  # Data Mining requires Basis Data
    "TI412": ["TI309"],  # ML Terapan requires ML Dasar
    "TI501": ["TI309"],  # ML Lanjut requires ML Dasar
    "TI507": ["TI501"],  # Deep Learning requires ML Lanjut
    "TI604": ["TI507"],  # Deep Learning Lanjut requires Deep Learning
    
    # AK Prerequisites
    "AK201": ["AK101"],  # Pengantar Akuntansi II requires I
    "AK202": ["AK201"],  # Akuntansi Keuangan Menengah I requires Pengantar II
    "AK301": ["AK202"],  # Akuntansi Keuangan Menengah II requires Menengah I
    "AK302": ["AK201"],  # Akuntansi Biaya requires Pengantar II
    "AK303": ["AK302"],  # Akuntansi Manajemen requires Akuntansi Biaya
    "AK305": ["AK202"],  # SIA requires Akuntansi Keuangan Menengah I
    "AK306": ["AK202"],  # Auditing I requires Akuntansi Keuangan Menengah I
    "AK401": ["AK301"],  # Akuntansi Keuangan Lanjutan I requires Menengah II
    "AK404": ["AK306"],  # Auditing II requires Auditing I
    "AK501": ["AK401"],  # Akuntansi Keuangan Lanjutan II requires Lanjutan I
    
    # TM Prerequisites
    "TM201": ["TM101"],  # Matematika Teknik II requires I
    "TM202": ["TM102"],  # Fisika Teknik II requires I
    "TM203": ["TM101", "TM102"],  # Mekanika Teknik requires Math & Physics I
    "TM205": ["TM102"],  # Termodinamika I requires Fisika Teknik I
    "TM301": ["TM205"],  # Mekanika Fluida requires Termodinamika I
    "TM302": ["TM203"],  # Elemen Mesin I requires Mekanika Teknik
    "TM303": ["TM205"],  # Termodinamika II requires Termodinamika I
    "TM305": ["TM205"],  # Perpindahan Panas I requires Termodinamika I
    "TM401": ["TM302"],  # Elemen Mesin II requires Elemen Mesin I
    "TM402": ["TM305"],  # Perpindahan Panas II requires Perpindahan Panas I
    "TM403": ["TM301"],  # Mesin-mesin Fluida requires Mekanika Fluida
    "TM501": ["TM401"],  # Perancangan Mesin requires Elemen Mesin II
    
    # AP Prerequisites
    "AP202": ["AP103"],  # Komputer Perkantoran II requires I
    "AP203": ["AP102"],  # Korespondensi Bisnis requires Komunikasi Bisnis
    "AP302": ["AP202"],  # SIM requires Komputer Perkantoran II
    "AP306": ["AP204"],  # Administrasi Kepegawaian requires Tata Kelola Perkantoran
    "AP402": ["AP302"],  # E-Office requires SIM
}


def get_max_sks_by_ipk(ipk: float, semester: int) -> int:
    """Calculate maximum SKS allowed based on IPK.
    
    Args:
        ipk: Current cumulative IPK
        semester: Current semester (1-based)
    
    Returns:
        Maximum SKS allowed
    """
    # Edge case: semester 1 students don't have IPK yet
    if semester == 1:
        return 20
    
    # SKS limits based on IPK
    if ipk >= 3.5:
        return 24
    elif ipk >= 3.0:
        return 22
    elif ipk >= 2.5:
        return 20
    else:
        return 18


def validate_prerequisites(course_code: str, completed_courses: list) -> tuple[bool, list]:
    """Validate if prerequisites are met for a course.
    
    Args:
        course_code: Course code to check
        completed_courses: List of course codes that have been completed (passed)
    
    Returns:
        Tuple of (is_valid, missing_prerequisites)
        - is_valid: True if all prerequisites are met
        - missing_prerequisites: List of missing prerequisite course codes
    """
    if course_code not in PREREQUISITES:
        return True, []
    
    required = PREREQUISITES[course_code]
    missing = [req for req in required if req not in completed_courses]
    
    return len(missing) == 0, missing


def get_completed_courses(riwayat_semester: list, min_grade: str = "D") -> list:
    """Extract list of completed (passed) course codes from student history.
    
    Args:
        riwayat_semester: Student's semester history
        min_grade: Minimum passing grade (default: D)
    
    Returns:
        List of course codes that have been passed
    """
    grade_order = ["A", "AB", "B", "BC", "C", "D", "E"]
    min_grade_idx = grade_order.index(min_grade) if min_grade in grade_order else 5
    
    completed = []
    for sem_data in riwayat_semester:
        for nilai in sem_data.get("nilai_matkul", []):
            grade = nilai.get("nilai_huruf", "E")
            if grade in grade_order:
                grade_idx = grade_order.index(grade)
                if grade_idx <= min_grade_idx:
                    completed.append(nilai["kode"])
    
    return completed
