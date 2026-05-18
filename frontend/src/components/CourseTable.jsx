// ============================================================
// FILE: CourseTable_PERBAIKAN.jsx
// TUJUAN: Perbandingan & Perbaikan kode saya vs kode Zein
// ============================================================

// ❌ KODE SAYA (SALAH):
// import React, { useState } from 'react';
// import './CourseTable.css';
// → Saya menggunakan CSS eksternal dan state yang tidak diperlukan

// ✅ KODE ZEIN (BENAR):
import { BookOpen, Target } from 'lucide-react';
// → Zein menggunakan ikon dari lucide-react untuk tampilan lebih rapi
// → Tidak perlu file CSS terpisah karena menggunakan Tailwind CSS

// ============================================================
// ❌ KODE SAYA (SALAH): Tidak ada konstanta warna grade
// ✅ KODE ZEIN (BENAR): Ada konstanta untuk warna nilai/grade
// → Ini penting agar warna nilai konsisten di seluruh komponen
// ============================================================

const GRADE_COLORS = {
  A: 'grade-A',
  AB: 'grade-AB',
  B: 'grade-B',
  BC: 'grade-BC',
  C: 'grade-C',
  D: 'grade-D',
  E: 'grade-E',
};

const GRADE_BAR_COLORS = {
  A: 'bg-emerald-500',
  AB: 'bg-green-500',
  B: 'bg-blue-500',
  BC: 'bg-sky-500',
  C: 'bg-yellow-500',
  D: 'bg-orange-500',
  E: 'bg-red-500',
};

// ============================================================
// ❌ KODE SAYA (SALAH): Tidak ada komponen GradeBar
// ✅ KODE ZEIN (BENAR): Ada komponen GradeBar untuk visualisasi nilai
// → Membuat progress bar berwarna sesuai nilai prediksi mahasiswa
// ============================================================

function GradeBar({ value, max = 4 }) {
  const pct = (value / max) * 100;
  const key =
    value >= 4.0 ? 'A' :
    value >= 3.5 ? 'AB' :
    value >= 3.0 ? 'B' :
    value >= 2.5 ? 'BC' :
    value >= 2.0 ? 'C' :
    value >= 1.0 ? 'D' : 'E';

  return (
    <div className="w-full bg-gray-100 dark:bg-gray-700 rounded-full h-1.5 overflow-hidden">
      <div
        className={`h-full rounded-full ${GRADE_BAR_COLORS[key] || 'bg-gray-400'} transition-all duration-500`}
        style={{ width: `${pct}%` }}
      />
    </div>
  );
}

// ============================================================
// ❌ KODE SAYA (SALAH): Tidak ada komponen ConfidenceBar
// ✅ KODE ZEIN (BENAR): Ada komponen ConfidenceBar untuk tingkat keyakinan prediksi
// → Menampilkan seberapa yakin sistem terhadap prediksi nilai
// ============================================================

function ConfidenceBar({ value }) {
  const color =
    value >= 80 ? 'bg-emerald-500' :
    value >= 70 ? 'bg-blue-500' :
    'bg-yellow-500';

  return (
    <div className="flex items-center gap-2">
      <div className="flex-1 bg-gray-100 dark:bg-gray-700 rounded-full h-1.5 overflow-hidden">
        <div
          className={`h-full rounded-full ${color} transition-all duration-500`}
          style={{ width: `${value}%` }}
        />
      </div>
      <span className="text-xs text-gray-500 dark:text-gray-400 w-8 text-right tabular-nums">
        {value}%
      </span>
    </div>
  );
}

// ============================================================
// KOMPONEN UTAMA - CourseTable
// ============================================================

export default function CourseTable({ courses }) {

  // ❌ KODE SAYA (SALAH):
  // const [sortConfig, setSortConfig] = useState(null);
  // const [filteredCourses, setFilteredCourses] = useState(courses);
  // const handleSort = (key) => { ... }
  // const handleSearch = (e) => { ... }
  // → Saya membuat fitur sort & search yang TIDAK ADA di kode Zein
  // → Ini menyebabkan fungsi komponen berbeda total dengan milik Zein
  // → Kode Zein fokus pada MENAMPILKAN prediksi nilai, bukan sorting/filtering

  // ✅ KODE ZEIN (BENAR): Langsung render data tanpa sort/filter
  if (!courses || courses.length === 0) {
    return (
      <div className="card">
        <p className="text-center text-gray-400">Tidak ada data mata kuliah prediksi.</p>
      </div>
    );
  }

  return (
    <div className="card animate-slide-up">

      {/* ❌ KODE SAYA (SALAH): Tidak ada header dengan ikon
          ✅ KODE ZEIN (BENAR): Ada header dengan ikon Target dari lucide-react */}
      <div className="flex items-center gap-3 mb-5">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow">
          <Target className="w-5 h-5 text-white" />
        </div>
        <div>
          <h3 className="section-title">Prediksi Nilai Semester 5</h3>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            Rekomendasi mata kuliah dan prediksi nilai
          </p>
        </div>
      </div>

      {/* ============================================================
          ❌ KODE SAYA (SALAH): Kolom tabel = ID, Nama, Instruktur, Siswa, Aksi
          → Ini untuk sistem manajemen kursus (CRUD), bukan prediksi akademik

          ✅ KODE ZEIN (BENAR): Kolom tabel = Kode, Mata Kuliah, SKS, Nilai, Angka, Confidence
          → Ini untuk sistem prediksi nilai mahasiswa
          → Data yang dipakai: course.kode, course.nama, course.sks,
                                course.prediksi_nilai_huruf, course.prediksi_nilai_angka, course.confidence
          ============================================================ */}

      {/* Tabel Desktop */}
      <div className="hidden md:block overflow-x-auto -mx-6">
        <table className="w-full">
          <thead>
            <tr className="bg-gray-50 dark:bg-gray-700/50">
              {/* ❌ SALAH: <th onClick={() => handleSort('id')}>ID</th> */}
              {/* ✅ BENAR: Kolom sesuai data prediksi akademik */}
              <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Kode</th>
              <th className="px-4 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Mata Kuliah</th>
              <th className="px-4 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">SKS</th>
              <th className="px-4 py-3 text-center text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Nilai</th>
              <th className="px-4 py-3 text-right text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider">Angka</th>
              <th className="px-6 py-3 text-left text-xs font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider w-48">Confidence</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100 dark:divide-gray-700">
            {courses.map((course) => (
              // ❌ SALAH: key={course.id}
              // ✅ BENAR: key={course.kode} → karena field-nya bernama 'kode', bukan 'id'
              <tr key={course.kode} className="hover:bg-gray-50 dark:hover:bg-gray-700/30 transition-colors">

                {/* ❌ SALAH: <td>{course.id}</td> */}
                {/* ✅ BENAR: Kode mata kuliah dengan styling monospace */}
                <td className="px-6 py-3.5">
                  <code className="text-xs font-mono bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded text-gray-700 dark:text-gray-300">
                    {course.kode}
                  </code>
                </td>

                {/* ❌ SALAH: <td>{course.name}</td> → field salah (name vs nama) */}
                {/* ✅ BENAR: course.nama + GradeBar untuk visualisasi */}
                <td className="px-4 py-3.5">
                  <div>
                    <p className="text-sm font-medium text-gray-900 dark:text-white">{course.nama}</p>
                    <GradeBar value={course.prediksi_nilai_angka} />
                  </div>
                </td>

                {/* ❌ SALAH: Tidak ada kolom SKS di kode saya */}
                {/* ✅ BENAR: Menampilkan jumlah SKS mata kuliah */}
                <td className="px-4 py-3.5 text-center">
                  <span className="inline-flex items-center justify-center w-7 h-7 rounded-lg bg-gray-100 dark:bg-gray-700 text-xs font-bold text-gray-700 dark:text-gray-300">
                    {course.sks}
                  </span>
                </td>

                {/* ❌ SALAH: Tidak ada kolom Nilai Huruf */}
                {/* ✅ BENAR: Badge nilai huruf dengan warna sesuai grade */}
                <td className="px-4 py-3.5 text-center">
                  <span className={`inline-block px-2.5 py-0.5 rounded-lg text-sm font-bold ${GRADE_COLORS[course.prediksi_nilai_huruf] || 'bg-gray-100 text-gray-700'}`}>
                    {course.prediksi_nilai_huruf}
                  </span>
                </td>

                {/* ❌ SALAH: Tidak ada kolom Nilai Angka */}
                {/* ✅ BENAR: Nilai angka dengan 1 desimal */}
                <td className="px-4 py-3.5 text-right">
                  <span className="text-sm font-semibold text-gray-700 dark:text-gray-300 tabular-nums">
                    {course.prediksi_nilai_angka.toFixed(1)}
                  </span>
                </td>

                {/* ❌ SALAH: <td><button>Lihat</button><button>Edit</button><button>Hapus</button></td> */}
                {/* ✅ BENAR: ConfidenceBar menampilkan tingkat keyakinan prediksi */}
                <td className="px-6 py-3.5">
                  <ConfidenceBar value={course.confidence} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* ❌ KODE SAYA (SALAH): Tidak ada tampilan Mobile Cards
          ✅ KODE ZEIN (BENAR): Ada tampilan responsif untuk mobile */}
      <div className="md:hidden space-y-3 mt-2">
        {courses.map((course) => (
          <div key={course.kode} className="bg-gray-50 dark:bg-gray-700/50 rounded-xl p-3">
            <div className="flex items-start justify-between gap-2 mb-2">
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-0.5">
                  <code className="text-xs font-mono bg-white dark:bg-gray-800 px-1.5 py-0.5 rounded text-gray-600 dark:text-gray-400">
                    {course.kode}
                  </code>
                  <span className="text-xs text-gray-500 dark:text-gray-400">{course.sks} SKS</span>
                </div>
                <p className="text-sm font-semibold text-gray-800 dark:text-gray-200">{course.nama}</p>
              </div>
              <div className="text-right flex-shrink-0">
                <span className={`inline-block px-2.5 py-0.5 rounded-lg text-sm font-bold ${GRADE_COLORS[course.prediksi_nilai_huruf] || ''}`}>
                  {course.prediksi_nilai_huruf}
                </span>
                <p className="text-xs text-gray-400 mt-0.5 tabular-nums">
                  {course.prediksi_nilai_angka.toFixed(1)}
                </p>
              </div>
            </div>
            <ConfidenceBar value={course.confidence} />
          </div>
        ))}
      </div>

      {/* ❌ KODE SAYA (SALAH): Tidak ada baris ringkasan/summary
          ✅ KODE ZEIN (BENAR): Ada summary → total matkul, total SKS, rata-rata nilai */}
      <div className="mt-4 pt-4 border-t border-gray-100 dark:border-gray-700 flex flex-wrap gap-4">
        <div className="flex items-center gap-2">
          <BookOpen className="w-4 h-4 text-gray-400" />
          <span className="text-sm text-gray-500 dark:text-gray-400">
            Total:{' '}
            <span className="font-semibold text-gray-700 dark:text-gray-200">
              {courses.length} mata kuliah
            </span>
          </span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500 dark:text-gray-400">
            Total SKS:{' '}
            <span className="font-semibold text-gray-700 dark:text-gray-200">
              {courses.reduce((s, c) => s + c.sks, 0)} SKS
            </span>
          </span>
        </div>
        <div className="flex items-center gap-2 ml-auto">
          <span className="text-sm text-gray-500 dark:text-gray-400">
            Rata-rata nilai prediksi:{' '}
            <span className="font-semibold text-gray-700 dark:text-gray-200 tabular-nums">
              {(courses.reduce((s, c) => s + c.prediksi_nilai_angka, 0) / courses.length).toFixed(2)}
            </span>
          </span>
        </div>
      </div>
    </div>
  );
}

// ============================================================
// RINGKASAN PERBEDAAN UNTUK DOSEN
// ============================================================
//
// NO | ASPEK              | KODE SAYA ❌           | KODE ZEIN ✅
// ---|--------------------|-----------------------|-------------------------
//  1 | Tujuan Komponen    | Manajemen kursus CRUD | Prediksi nilai akademik
//  2 | Kolom Tabel        | ID,Nama,Instruktur,   | Kode,MK,SKS,Nilai,
//    |                    | Siswa,Aksi            | Angka,Confidence
//  3 | Field Data         | course.id/.name/      | course.kode/.nama/.sks/
//    |                    | .instructor/.students | .prediksi_nilai_huruf/
//    |                    |                       | .prediksi_nilai_angka/
//    |                    |                       | .confidence
//  4 | Fitur Tambahan     | Sort & Search         | Tidak ada (tidak perlu)
//  5 | Sub-komponen       | Tidak ada             | GradeBar + ConfidenceBar
//  6 | Responsif Mobile   | Tidak ada             | Ada card mobile view
//  7 | Summary/Ringkasan  | Tidak ada             | Ada total SKS & rata-rata
//  8 | Styling            | CSS eksternal         | Tailwind CSS + lucide-react
//  9 | Tombol Aksi        | Lihat/Edit/Hapus      | Tidak ada (hanya display)
// 10 | Warna Nilai        | Tidak ada             | Ada GRADE_COLORS per huruf
// ============================================================
