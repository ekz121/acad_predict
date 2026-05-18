// ============================================================
// FILE: LoadingSpinner.jsx
// PERBANDINGAN KODE: Kode Saya vs Kode Zein
// STATUS: ✅ IDENTIK - Fungsi dan hasil render sama persis
// ============================================================


// ──────────────────────────────────────────────────────────────
// KOMPONEN 1: LoadingSpinner (Default Export)
// Fungsi: Menampilkan spinner loading di tengah halaman
//         dengan pesan teks yang bisa dikustomisasi
// ──────────────────────────────────────────────────────────────

// ✅ [BENAR] - Parameter default 'Memuat data...' sudah sama dengan Zein
export default function LoadingSpinner({ message = 'Memuat data...' }) {
  return (
    // ✅ [BENAR] - Wrapper flex column, center horizontal & vertical, padding atas-bawah 20
    <div className="flex flex-col items-center justify-center py-20 gap-4">

      {/* Container spinner - menggunakan 'relative' agar spinner dalam bisa di-overlay */}
      <div className="relative">

        {/* ✅ [BENAR] - Spinner LUAR: ukuran 16, warna indigo, berputar searah jarum jam */}
        {/* Kode Zein  : border-indigo-100 dark:border-indigo-900 border-t-indigo-600 dark:border-t-indigo-400 */}
        {/* Kode Saya  : border-indigo-100 dark:border-indigo-900 border-t-indigo-600 dark:border-t-indigo-400 */}
        {/* STATUS     : ✅ SAMA */}
        <div className="w-16 h-16 rounded-full border-4 border-indigo-100 dark:border-indigo-900 animate-spin border-t-indigo-600 dark:border-t-indigo-400" />

        {/* ✅ [BENAR] - Spinner DALAM: ukuran 8, warna purple, berputar BERLAWANAN jarum jam */}
        {/* 'absolute inset-2' = posisi di tengah spinner luar */}
        {/* animationDirection: 'reverse' = berputar berlawanan (efek double spinner) */}
        {/* animationDuration: '0.8s'     = lebih cepat dari spinner luar */}
        {/* Kode Zein  : style={{ animationDirection: 'reverse', animationDuration: '0.8s' }} */}
        {/* Kode Saya  : style={{ animationDirection: 'reverse', animationDuration: '0.8s' }} */}
        {/* STATUS     : ✅ SAMA */}
        <div
          className="absolute inset-2 w-8 h-8 rounded-full border-4 border-purple-100 dark:border-purple-900 animate-spin border-t-purple-600 dark:border-t-purple-400"
          style={{ animationDirection: 'reverse', animationDuration: '0.8s' }}
        />
      </div>

      {/* ✅ [BENAR] - Teks pesan dengan animasi pulse (kedip halus) */}
      {/* Kode Zein : text-sm font-medium text-gray-500 dark:text-gray-400 animate-pulse */}
      {/* Kode Saya : text-sm font-medium text-gray-500 dark:text-gray-400 animate-pulse */}
      {/* STATUS    : ✅ SAMA */}
      <p className="text-sm font-medium text-gray-500 dark:text-gray-400 animate-pulse">
        {message}
      </p>

    </div>
  )
}


// ──────────────────────────────────────────────────────────────
// KOMPONEN 2: InlineSpinner (Named Export)
// Fungsi: Spinner kecil untuk dipakai di dalam tombol/elemen inline
// ──────────────────────────────────────────────────────────────

// ✅ [BENAR] - Named export (bukan default), dipakai seperti: import { InlineSpinner } from '...'
export function InlineSpinner() {
  return (
    // ✅ [BENAR] - Ukuran kecil (w-5 h-5), border putih transparan, cocok di atas background gelap
    // Kode Zein : border-white/30 border-t-white
    // Kode Saya : border-white/30 border-t-white
    // STATUS    : ✅ SAMA
    <div className="w-5 h-5 rounded-full border-2 border-white/30 border-t-white animate-spin" />
  )
}


// ============================================================
// KESIMPULAN PERBANDINGAN:
//
// | Bagian                  | Kode Zein | Kode Saya | Status  |
// |-------------------------|-----------|-----------|---------|
// | Default export name     | ✅        | ✅        | SAMA    |
// | Parameter default msg   | ✅        | ✅        | SAMA    |
// | Spinner luar (indigo)   | ✅        | ✅        | SAMA    |
// | Spinner dalam (purple)  | ✅        | ✅        | SAMA    |
// | Arah & kecepatan animasi| ✅        | ✅        | SAMA    |
// | Teks animate-pulse      | ✅        | ✅        | SAMA    |
// | InlineSpinner export    | ✅        | ✅        | SAMA    |
//
// HASIL: Jika di-run, tampilan dan perilaku akan SAMA PERSIS
//        dengan kode milik Zein. Tidak ada yang perlu diperbaiki.
// ============================================================
