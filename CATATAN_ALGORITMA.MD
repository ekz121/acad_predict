# Catatan Analisis Algoritma Prediksi — AcadPredict

## Tujuan Dokumen
Dokumen ini mencatat letak, cara kerja, dan bagian kritis dari algoritma prediksi performa akademik dalam project AcadPredict. Dibuat untuk keperluan tugas dosen: mengidentifikasi bagian algoritma yang membuat sistem bisa memprediksi.

---

## File-File yang Dianalisis

| File | Peran |
|------|-------|
| `backend/utils/predictor.py` | **INTI** — Mesin prediksi utama |
| `backend/utils/ipk_target.py` | Analisis & proyeksi target IPK |
| `backend/utils/curriculum.py` | Data kurikulum + aturan prasyarat + batas SKS |
| `backend/utils/data_generator.py` | Generator data mahasiswa sintetis |
| `backend/main.py` | API endpoint yang memanggil fungsi prediksi |
| `frontend/src/api/client.js` | Pemanggil API dari sisi frontend |
| `frontend/src/pages/Dashboard.jsx` | Tampilan hasil prediksi |
| `frontend/src/components/IPKTargetAssistant.jsx` | Wizard target IPK |

---

## Algoritma Prediksi Utama

### Lokasi: `backend/utils/predictor.py`

Ini adalah **file paling kritis**. Tanpa file ini (atau jika fungsi-fungsi di dalamnya dihapus/dikosongkan), sistem tidak bisa menghasilkan prediksi apapun.

---

### Fungsi 1: `predict_course_grade` (baris ~37–74)

**Tujuan:** Memprediksi nilai satu mata kuliah.

**Formula utama:**
```
base = (IPK_historis × 0.6) + (rata_nilai_matkul_terkait × 0.4)
```
- Jika IPK mahasiswa di bawah rata-rata cohort:
  ```
  base = base × 0.85 + cohort_avg × 0.15
  ```
- Adjustment tren:
  ```
  trend_adjustment = clamp(trend × 0.2, -0.5, 0.5)
  raw = base + trend_adjustment
  ```
- Nilai akhir dibulatkan ke grade point terdekat: `[4.0, 3.5, 3.0, 2.5, 2.0, 1.0, 0.0]`

**Jika fungsi ini dihapus/dikosongkan:** Sistem tidak bisa menghitung prediksi nilai per mata kuliah → seluruh alur prediksi berhenti.

---

### Fungsi 2: `predict_student` (baris ~147–260)

**Tujuan:** Menghasilkan prediksi lengkap satu mahasiswa.

**Langkah-langkah algoritma:**
1. Ambil riwayat semester yang sudah selesai (semester < semester aktif).
2. Hitung **weighted average IPS** dari riwayat:
   - Jika ≥ 3 semester: `IPS3×0.5 + IPS2×0.3 + IPS1×0.2`
   - Jika 2 semester: `IPS2×0.6 + IPS1×0.4`
   - Jika 1 semester: gunakan IPS tunggal
   - Jika 0 semester: gunakan default 2.5
3. Hitung **tren**: selisih IPS semester terakhir dengan sebelumnya.
4. Untuk setiap mata kuliah di semester target: panggil `predict_course_grade`.
5. Filter mata kuliah yang memenuhi prasyarat.
6. Bangun **skenario SKS** (18, 20, 22, 24 SKS) via `build_sks_scenario`.
7. Pilih skenario rekomendasi berdasarkan IPK saat ini.
8. Hitung prediksi IPK baru:
   ```
   IPK_baru = (SKS_lama × IPK_lama + SKS_semester × IPS_prediksi) / (SKS_lama + SKS_semester)
   ```

**Jika fungsi ini dihapus/dikosongkan:** Endpoint `/api/predict/{nim}` akan error → Dashboard tidak menampilkan data apapun.

---

### Fungsi 3: `build_sks_scenario` (baris ~77–145)

**Tujuan:** Memilih kombinasi mata kuliah optimal untuk target SKS tertentu.

**Cara kerja:**
1. Selalu sertakan semua mata kuliah **wajib**.
2. Urutkan mata kuliah **pilihan** berdasarkan prediksi nilai tertinggi.
3. Tambahkan mata kuliah pilihan sampai mencapai target SKS (mengutamakan yang tepat pas SKS-nya).
4. Hitung prediksi IPS dan IPK untuk skenario tersebut.

---

## Algoritma Proyeksi Target IPK

### Lokasi: `backend/utils/ipk_target.py`

Digunakan oleh fitur "Asisten Target IPK" (wizard di Dashboard).

### Fungsi kritis: `_ips_minimum` dan `_proyeksi_ipk`

**`_ips_minimum`:** Menghitung IPS minimum rata-rata yang harus dicapai per semester agar target IPK tercapai:
```
SKS_sisa = sisa_semester × 22
IPS_min = (target_IPK × (SKS_lulus + SKS_sisa) - IPK_sekarang × SKS_lulus) / SKS_sisa
```

**`_proyeksi_ipk`:** Mensimulasikan IPK per semester ke depan jika IPS minimum selalu tercapai.

**`_validasi_target`:** Menentukan apakah target realistis, ambisius, atau tidak mungkin.

---

## Aturan Pendukung Prediksi

### Lokasi: `backend/utils/curriculum.py`

Fungsi-fungsi ini **mendukung** algoritma prediksi:

| Fungsi | Peran |
|--------|-------|
| `get_max_sks_by_ipk` | Menentukan batas maksimum SKS berdasarkan IPK (IPK≥3.5→24 SKS, dst.) |
| `validate_prerequisites` | Mengecek apakah prasyarat mata kuliah sudah terpenuhi |
| `get_completed_courses` | Mengambil daftar mata kuliah yang sudah lulus dari riwayat |
| `get_cohort_average` (di predictor.py) | Memberikan rata-rata cohort per prodi sebagai acuan |

---

## Bagian yang Jika Dihapus Akan Mematikan Prediksi

Berikut bagian-bagian yang bisa **dihapus untuk menonaktifkan kemampuan prediksi**, dari yang paling berdampak:

### Opsi 1 — Hapus/Kosongkan fungsi `predict_course_grade` di `predictor.py`
- Dampak: Tidak ada nilai prediksi per mata kuliah → `predict_student` error.
- Cara: Buat fungsi mengembalikan nilai kosong atau raise exception.

### Opsi 2 — Hapus/Kosongkan fungsi `predict_student` di `predictor.py`
- Dampak langsung: Endpoint `/api/predict/{nim}` tidak menghasilkan prediksi.
- Frontend: Dashboard tampil tapi semua data prediksi kosong/error.

### Opsi 3 — Hapus blok weighted average IPS di dalam `predict_student`
- Baris kritis (sekitar baris 165–177 di predictor.py):
  ```python
  if len(ips_list) >= 3:
      ips1, ips2, ips3 = ips_list[-3], ips_list[-2], ips_list[-1]
      weighted_avg = ips3 * 0.5 + ips2 * 0.3 + ips1 * 0.2
      trend = ips3 - ips2
  elif len(ips_list) == 2:
      ...
  ```
- Dampak: Tidak ada dasar perhitungan IPS → semua prediksi nilai jadi tidak akurat/default.

### Opsi 4 — Hapus formula di `predict_course_grade`
- Baris kritis (formula base):
  ```python
  if related_courses_avg > 0:
      base = (historical_ipk * 0.6) + (related_courses_avg * 0.4)
  else:
      base = historical_ipk
  ```
- Dampak: Nilai prediksi tidak dihitung berdasarkan data historis.

---

## Ringkasan Alur Prediksi

```
Request /api/predict/{nim}
        ↓
  main.py → predict_student(student)
        ↓
  Hitung weighted_avg IPS + trend dari riwayat
        ↓
  Untuk tiap matkul semester target:
    predict_course_grade(IPK, related_avg, cohort_avg, trend)
        ↓
  Validasi prasyarat (curriculum.py)
        ↓
  build_sks_scenario() untuk SKS 18/20/22/24
        ↓
  Pilih skenario rekomendasi → hitung IPK baru
        ↓
  Return hasil prediksi ke frontend
```

---

## Koreksi & Kesimpulan Final (Verified 100%)

Setelah analisis menyeluruh seluruh codebase (semua file kecuali students.json), algoritma prediksi **tidak hanya ada di `predictor.py`** — tersebar di **2 file backend** dengan total **8 fungsi algoritmik**.

### Peta lengkap semua fungsi algoritmik:

| File | Fungsi | Status |
|------|--------|--------|
| `predictor.py` | `get_related_courses_avg` | Pendukung — hitung rata-rata nilai historis |
| `predictor.py` | `get_cohort_average` | Pendukung — rata-rata IPK per prodi |
| `predictor.py` | `predict_course_grade` | **INTI** — formula prediksi nilai matkul |
| `predictor.py` | `build_sks_scenario` | **INTI** — pemilihan matkul optimal per skenario SKS |
| `predictor.py` | `predict_student` | **INTI** — orkestrasi prediksi lengkap |
| `curriculum.py` | `get_max_sks_by_ipk` | **KRITIS** — menentukan batas SKS berdasarkan IPK |
| `curriculum.py` | `validate_prerequisites` | **KRITIS** — menyaring matkul berdasarkan prasyarat |
| `curriculum.py` | `get_completed_courses` | **KRITIS** — mengekstrak matkul lulus dari riwayat |

### Apa yang terjadi jika dihapus:

**Hapus `predict_course_grade` saja:**
- `predict_student` langsung error karena memanggil fungsi ini untuk setiap matkul
- Backend return error 500, Dashboard tidak bisa dibuka sama sekali

**Hapus `build_sks_scenario` saja:**
- `predict_student` error saat membangun skenario SKS
- Tidak ada simulasi 18/20/22/24 SKS, tidak ada rekomendasi matkul

**Hapus `predict_student` saja:**
- Endpoint `/api/predict/{nim}` di `main.py` langsung error
- Semua halaman Dashboard mahasiswa mana pun tidak bisa dibuka

**Hapus `get_max_sks_by_ipk` dari `curriculum.py`:**
- `predict_student` error saat menentukan batas SKS
- Skenario tidak bisa dibangun sama sekali

**Hapus `validate_prerequisites` dari `curriculum.py`:**
- Sistem tetap jalan tapi semua matkul dianggap boleh diambil tanpa cek prasyarat
- Prediksi tidak akurat/realistis

**Hapus ketiga fungsi INTI sekaligus (`predict_course_grade` + `build_sks_scenario` + `predict_student`):**
- Backend masih bisa start
- Endpoint `/health` dan `/api/students` (daftar mahasiswa) masih jalan
- Endpoint `/api/predict/{nim}` crash error 500
- Seluruh Dashboard per mahasiswa tidak bisa diakses
- Hanya halaman Landing/daftar mahasiswa yang tetap bisa dibuka

### Kesimpulan:
Untuk mematikan kemampuan prediksi, cukup hapus/kosongkan salah satu dari 3 fungsi INTI di `predictor.py`. Menghapus `predict_student` adalah cara paling langsung karena ia adalah titik masuk tunggal yang dipanggil oleh `main.py`.
