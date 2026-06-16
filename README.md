# AcadPredict — Sistem Prediksi Performa Akademik Mahasiswa

## Prasyarat (Install Sekali Saja)

**1. Python 3.10+**
- Download: https://www.python.org/downloads/
- Saat install, centang **"Add Python to PATH"**
- Verifikasi: buka CMD → `python --version`

**2. Node.js 18+**
- Download: https://nodejs.org/ (pilih versi LTS)
- Verifikasi: buka CMD → `node --version` dan `npm --version`

---

## Setup Awal (Hanya Sekali)

### Backend
```
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Frontend
```
cd frontend
npm install
```

---

## Cara Menjalankan

Buka **2 terminal terpisah**, jalankan backend dulu baru frontend.

### Terminal 1 — Backend
```
cd backend
.venv\Scripts\activate
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```
Tunggu hingga muncul: `Uvicorn running on http://0.0.0.0:8001`

### Terminal 2 — Frontend
```
cd frontend
npm run dev
```
Tunggu hingga muncul: `Local: http://localhost:3000`

### Atau cukup 2x klik (urutan wajib: backend dulu)
1. `start_backend.bat`
2. `start_frontend.bat`

---

## Akses Aplikasi

| Halaman | URL |
|--------|-----|
| Aplikasi | http://localhost:3000 |
| Cek Backend | http://localhost:8001/health |
| API Docs | http://localhost:8001/docs |

---

## Troubleshooting

**`python` tidak dikenali**
→ Reinstall Python, centang "Add Python to PATH", restart CMD

**`npm` tidak dikenali**
→ Reinstall Node.js, restart komputer

**Frontend tidak bisa ambil data (Network Error)**
→ Pastikan backend sudah jalan di port 8001 sebelum membuka frontend

**Port sudah dipakai (address already in use)**
→ Buka Task Manager → cari `python.exe` atau `node.exe` → End Task → coba lagi

**Browser tampilkan ERR_ADDRESS_INVALID saat buka `0.0.0.0:8001`**
→ Gunakan `http://localhost:8001` bukan `http://0.0.0.0:8001`
