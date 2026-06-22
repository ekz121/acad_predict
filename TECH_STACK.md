# Tech Stack — AcadPredict

Sistem Prediksi Performa Akademik Mahasiswa

---

## Gambaran Arsitektur

```
Browser (React + Vite)
        ↕  HTTP / REST API
FastAPI Server (Python)
        ↕  File I/O
students.json (flat file database)
```

---

## Backend

### Bahasa & Runtime
| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| Python | 3.10+ | Bahasa utama backend |

### Framework & Server
| Library | Versi | Kegunaan |
|---------|-------|----------|
| FastAPI | 0.111.0 | Web framework REST API |
| Uvicorn | 0.29.0 | ASGI server untuk menjalankan FastAPI |

### Library
| Library | Versi | Kegunaan |
|---------|-------|----------|
| Pydantic | 2.7.1 | Validasi request/response model (`BaseModel`) |
| python-dotenv | 1.0.1 | Load environment variable dari `.env` |
| json, os, sys, math, random, hashlib, datetime | built-in | Standard library Python, tidak perlu install |

### Middleware
- **CORS** via `CORSMiddleware` — allow all origins `*`

### Data Storage
- **`students.json`** — flat file JSON, tidak menggunakan database

---

## Frontend

### Bahasa & Runtime
| Teknologi | Versi | Kegunaan |
|-----------|-------|----------|
| JavaScript (ESM) + JSX | — | Bahasa utama frontend |
| Node.js | 18+ | Runtime untuk tooling & build |

### Framework & Build Tool
| Library | Versi | Kegunaan |
|---------|-------|----------|
| React | 18.3.1 | UI library utama |
| Vite | 5.3.1 | Bundler + dev server (port 3000) |

### Routing
| Library | Versi | Kegunaan |
|---------|-------|----------|
| React Router DOM | 6.23.1 | Client-side routing (`/` dan `/dashboard/:nim`) |

### Styling
| Library | Versi | Kegunaan |
|---------|-------|----------|
| Tailwind CSS | 3.4.4 | Utility-first CSS framework |
| PostCSS | 8.4.38 | Pipeline Tailwind |
| Autoprefixer | 10.4.19 | Vendor prefix otomatis |

Konfigurasi Tailwind:
- Dark mode: `class` strategy
- Font: `Inter` (system-ui fallback)
- Custom animation: `fade-in`, `slide-up`, `pulse-slow`
- Custom gradient: `gradient-radial`

### Charting
| Library | Versi | Komponen yang Dipakai |
|---------|-------|----------------------|
| Recharts | 2.12.7 | `AreaChart`, `LineChart`, `XAxis`, `YAxis`, `CartesianGrid`, `Tooltip`, `ReferenceLine`, `Legend`, `ResponsiveContainer` |

### HTTP Client
| Library | Versi | Kegunaan |
|---------|-------|----------|
| Axios | 1.7.2 | HTTP request ke backend, dengan interceptor error handling global |

### Icons
| Library | Versi | Kegunaan |
|---------|-------|----------|
| Lucide React | 0.395.0 | Icon SVG siap pakai (`Brain`, `BarChart3`, `TrendingUp`, `Search`, dll.) |

### State Management
- React built-in: `useState`, `useEffect`, `useMemo`
- Tidak menggunakan Redux, Zustand, atau library state management eksternal

---

## Struktur Proyek

```
acad_predict/
├── backend/
│   ├── utils/
│   │   ├── predictor.py       # Mesin prediksi utama (INTI)
│   │   ├── ipk_target.py      # Analisis & proyeksi target IPK
│   │   ├── curriculum.py      # Kurikulum 4 prodi, prasyarat, batas SKS
│   │   └── data_generator.py  # Generator 100 data mahasiswa sintetis
│   ├── main.py                # Entry point FastAPI + semua endpoint REST
│   ├── requirements.txt
│   └── students.json          # Flat file database
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js      # Axios instance + semua fungsi API call
│   │   ├── components/
│   │   │   ├── IPKTargetAssistant.jsx  # Wizard 4-step analisis target IPK
│   │   │   ├── Navbar.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   └── ...
│   │   ├── pages/
│   │   │   ├── Landing.jsx    # Halaman beranda + search NIM
│   │   │   └── Dashboard.jsx  # Halaman prediksi lengkap per mahasiswa
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
├── README.md
├── TECH_STACK.md
├── CATATAN_ALGORITMA.md
├── start_backend.bat
└── start_frontend.bat
```

---

## REST API Endpoints

| Method | Endpoint | Kegunaan |
|--------|----------|----------|
| GET | `/health` | Cek status server + jumlah mahasiswa |
| GET | `/api/students` | Daftar mahasiswa (pagination, filter prodi, search) |
| GET | `/api/student/{nim}` | Data detail satu mahasiswa |
| GET | `/api/predict/{nim}` | Prediksi lengkap IPS/IPK mahasiswa |
| POST | `/api/ipk-target/{nim}` | Analisis target IPK + panduan personal |

Dokumentasi Swagger otomatis tersedia di: `http://localhost:8001/docs`

---

## Algoritma Prediksi

### Weighted Average IPS
Dasar perhitungan prediksi menggunakan IPS historis berbobot:

```
Jika ≥ 3 semester: weighted_avg = IPS3×0.5 + IPS2×0.3 + IPS1×0.2
Jika 2 semester:   weighted_avg = IPS2×0.6 + IPS1×0.4
Jika 1 semester:   weighted_avg = IPS1
Jika 0 semester:   weighted_avg = 2.5 (default)
```

### Prediksi Nilai Mata Kuliah
```
base = (weighted_avg × 0.6) + (rata_nilai_historis × 0.4)

Jika IPK < rata_cohort:
  base = base × 0.85 + cohort_avg × 0.15

trend_adjustment = clamp(trend × 0.35, -0.8, 0.8)
nilai_prediksi = clamp(base + trend_adjustment, 0.0, 4.0)
```

Dibulatkan ke grade point terdekat: `A(4.0) AB(3.5) B(3.0) BC(2.5) C(2.0) D(1.0) E(0.0)`

### Prediksi IPK Baru
```
IPK_baru = (SKS_lama × IPK_lama + SKS_semester × IPS_prediksi) / (SKS_lama + SKS_semester)
```

### Batas SKS Berdasarkan IPK
| IPK | Maks SKS |
|-----|----------|
| ≥ 3.50 | 24 SKS |
| ≥ 3.00 | 22 SKS |
| ≥ 2.50 | 20 SKS |
| < 2.50 | 18 SKS |

### Analisis Target IPK
```
SKS_sisa = sisa_semester × 22
IPS_minimum = (target_IPK × (SKS_lulus + SKS_sisa) - IPK_sekarang × SKS_lulus) / SKS_sisa
```

---

## Konfigurasi Vite (Dev Proxy)

```js
// vite.config.js
server: {
  port: 3000,
  proxy: {
    '/api'    → 'http://localhost:8001',
    '/health' → 'http://localhost:8001',
  }
}
```

---

## Port Default

| Service | Port | URL |
|---------|------|-----|
| Frontend (Vite) | 3000 | http://localhost:3000 |
| Backend (FastAPI) | 8001 | http://localhost:8001 |
| API Docs (Swagger) | 8001 | http://localhost:8001/docs |
