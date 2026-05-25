// ============================================================
// FILE: Navbar.jsx
// PERBANDINGAN: Kode kamu vs Kode Zein
// ============================================================
// KESIMPULAN UMUM:
// Kode kamu HANYA mengimplementasikan ~20% dari fungsi Zein.
// Kode kamu hanya berisi: logo + tombol dark mode.
// Kode Zein memiliki: logo, navigasi desktop, navigasi mobile,
// popup "Cara Kerja" & "Fitur", dark mode, routing, dan scroll.
// ============================================================

// ❌ KODE KAMU (dijadikan komentar, JANGAN DIHAPUS):
// import React from "react";
// import { GraduationCap, Sun, Moon } from "lucide-react";
//
// const Navbar = ({ darkMode, setDarkMode }) => {
//   return (
//     <nav className="flex items-center justify-between px-6 py-4 shadow-md bg-white dark:bg-gray-800">
//       {/* Logo */}
//       <div className="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white">
//         <GraduationCap className="w-6 h-6" />
//         <span>AcadPredict</span>
//       </div>
//       {/* Dark Mode Toggle */}
//       <button
//         onClick={() => setDarkMode(!darkMode)}
//         className="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:scale-105 transition"
//       >
//         {darkMode ? (
//           <Sun className="w-5 h-5 text-yellow-400" />
//         ) : (
//           <Moon className="w-5 h-5 text-gray-800" />
//         )}
//       </button>
//     </nav>
//   );
// };
// export default Navbar;

// ============================================================
// DAFTAR KESALAHAN / KEKURANGAN PADA KODE KAMU:
// ============================================================
// 1. ❌ IMPORT TIDAK LENGKAP
//    Kamu hanya import: GraduationCap, Sun, Moon
//    Zein import: Moon, Sun, GraduationCap, BarChart3, X, Menu,
//                 Cpu, Database, Layers, Search, Brain, BookOpen,
//                 Zap, BarChart3 as BarIcon, ChevronRight, Home
//    → Icon-icon ini digunakan untuk menu mobile & popup konten.
//
// 2. ❌ TIDAK ADA ROUTING (react-router-dom)
//    Kamu tidak import useLocation, useNavigate, Link.
//    Zein menggunakan ini untuk mendeteksi halaman aktif (isLanding)
//    dan navigasi antar halaman.
//
// 3. ❌ TIDAK ADA STATE MANAGEMENT
//    Kamu tidak pakai useState sama sekali.
//    Zein menggunakan:
//      - useState(null)  → untuk mengontrol popup yang mana yang terbuka
//      - useState(false) → untuk mengontrol buka/tutup menu mobile
//
// 4. ❌ TIDAK ADA NAVIGASI DESKTOP
//    Kamu tidak punya link/tombol: Beranda, Cara Kerja, Fitur.
//    Zein memiliki 3 item navigasi di desktop (hidden di mobile).
//
// 5. ❌ TIDAK ADA MENU HAMBURGER (MOBILE)
//    Kamu tidak punya menu untuk layar kecil.
//    Zein punya tombol hamburger (Menu/X icon) yang toggle
//    dropdown mobile menu dengan animasi.
//
// 6. ❌ TIDAK ADA POPUP MODAL
//    Kamu tidak punya komponen NavPopup.
//    Zein punya popup untuk "Cara Kerja" dan "Fitur" yang muncul
//    saat tombol ditekan di halaman selain landing page.
//
// 7. ❌ TIDAK ADA KONTEN POPUP (POPUP_CONTENT)
//    Kamu tidak mendefinisikan data popup sama sekali.
//
// 8. ❌ LOGIC SCROLL / NAVIGASI
//    Kamu tidak punya handleNavClick yang membedakan:
//    - Jika di landing page → scroll ke section
//    - Jika di halaman lain → buka popup
//
// 9. ❌ STYLING BERBEDA (minor)
//    Kamu: bg-white dark:bg-gray-800 (warna solid biasa)
//    Zein: bg-white/90 dark:bg-gray-900/90 backdrop-blur-md
//          (transparan + efek blur → lebih modern)
//    Kamu: shadow-md (bayangan biasa)
//    Zein: border-b border-gray-200/50 (border bawah halus)
//
// 10. ❌ LOGO BERBEDA
//    Kamu: Logo hanya div biasa, tidak ada gradient, tidak ada Link
//    Zein: Logo dibungkus <Link to="/"> dengan div gradient
//          dan efek hover shadow
//
// ============================================================
// ✅ KODE PERBAIKAN (setara dengan kode Zein):
// ============================================================

import { useState } from 'react'
import { Link, useLocation, useNavigate } from 'react-router-dom'
import {
  Moon, Sun, GraduationCap, BarChart3, X, Menu,
  Cpu, Database, Layers, Search,
  Brain, BookOpen, Zap, BarChart3 as BarIcon,
  ChevronRight, Home
} from 'lucide-react'
// ✅ PERBAIKAN 1: Import lengkap semua icon & library yang dibutuhkan
// Kode kamu hanya import 3 icon → sekarang 14+ icon + hooks routing

// ✅ PERBAIKAN 2: Data konten popup didefinisikan di luar komponen
// Kode kamu tidak punya ini sama sekali
const POPUP_CONTENT = {
  'cara-kerja': {
    title: 'Cara Kerja Sistem',
    subtitle: 'Proses prediksi yang transparan dan dapat dipahami',
    color: 'from-indigo-500 to-purple-600',
    steps: [
      { icon: Search,   step: '01', title: 'Masukkan NIM',          desc: 'Masukkan NIM 8 digit mahasiswa. Format: 2 digit tahun + 3 digit kode prodi + 3 digit nomor urut.' },
      { icon: Database, step: '02', title: 'Analisis Data Historis', desc: 'Sistem menganalisis nilai dari semua semester yang telah ditempuh untuk menghitung tren performa akademik.' },
      { icon: Cpu,      step: '03', title: 'Kalkulasi Prediksi',     desc: 'Algoritma weighted average menghitung prediksi IPS, IPK, dan nilai per mata kuliah dengan bobot Sem3:50%, Sem2:30%, Sem1:20%.' },
      { icon: Layers,   step: '04', title: 'Tampilkan Dashboard',    desc: 'Hasil prediksi ditampilkan dalam dashboard lengkap dengan grafik tren, simulasi SKS, dan rekomendasi mata kuliah.' },
    ],
  },
  'fitur': {
    title: 'Fitur Unggulan',
    subtitle: 'Dirancang untuk membantu memantau dan memprediksi performa akademik',
    color: 'from-purple-500 to-pink-600',
    steps: [
      { icon: Brain,    step: null, title: 'Prediksi Berbasis AI',     desc: 'Algoritma prediksi berbasis data historis dengan weighted average dan analisis tren semester.' },
      { icon: BarIcon,  step: null, title: 'Visualisasi Tren IPK',     desc: 'Grafik interaktif menampilkan tren performa akademik IPS & IPK dari semester ke semester.' },
      { icon: BookOpen, step: null, title: 'Prediksi Per Mata Kuliah', desc: 'Prediksi nilai untuk setiap mata kuliah semester berikutnya beserta tingkat kepercayaan.' },
      { icon: Zap,      step: null, title: 'Simulasi Beban SKS',       desc: 'Simulasi 4 skenario SKS dengan prediksi IPS dan IPK untuk setiap pilihan beban studi.' },
    ],
  },
}

// ✅ PERBAIKAN 3: Komponen popup terpisah (NavPopup)
// Kode kamu tidak punya komponen ini sama sekali
function NavPopup({ type, onClose }) {
  const content = POPUP_CONTENT[type]
  if (!content) return null
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4" onClick={onClose}>
      <div className="absolute inset-0 bg-black/40 backdrop-blur-sm" />
      <div
        className="relative bg-white dark:bg-gray-900 rounded-3xl shadow-2xl w-full max-w-lg overflow-hidden animate-slide-up"
        onClick={e => e.stopPropagation()}
      >
        {/* Header popup dengan gradient */}
        <div className={`bg-gradient-to-r ${content.color} p-5 sm:p-6 text-white`}>
          <div className="flex items-start justify-between gap-3">
            <div>
              <h2 className="text-lg sm:text-xl font-extrabold">{content.title}</h2>
              <p className="text-white/80 text-sm mt-1">{content.subtitle}</p>
            </div>
            <button onClick={onClose} className="w-8 h-8 rounded-xl bg-white/20 hover:bg-white/30 flex items-center justify-center transition-colors flex-shrink-0">
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>
        {/* Isi popup */}
        <div className="p-5 sm:p-6 space-y-4">
          {content.steps.map((item, i) => {
            const Icon = item.icon
            return (
              <div key={i} className="flex items-start gap-3">
                <div className={`w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-br ${content.color} flex items-center justify-center shadow flex-shrink-0`}>
                  <Icon className="w-4 h-4 sm:w-5 sm:h-5 text-white" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    {item.step && <span className="text-xs font-bold text-indigo-500 dark:text-indigo-400 uppercase tracking-widest">{item.step}</span>}
                    <p className="font-bold text-gray-900 dark:text-white text-sm">{item.title}</p>
                  </div>
                  <p className="text-xs sm:text-sm text-gray-500 dark:text-gray-400 mt-0.5 leading-relaxed">{item.desc}</p>
                </div>
              </div>
            )
          })}
        </div>
        {/* Tombol tutup bawah */}
        <div className="px-5 sm:px-6 pb-5 sm:pb-6">
          <button
            onClick={onClose}
            className={`w-full py-3 rounded-2xl bg-gradient-to-r ${content.color} text-white font-bold text-sm flex items-center justify-center gap-2 hover:opacity-90 transition-opacity`}
          >
            Mengerti <ChevronRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  )
}

// ✅ PERBAIKAN 4: Komponen Navbar utama dengan semua fitur lengkap
export default function Navbar({ darkMode, setDarkMode }) {
  // ✅ PERBAIKAN 5: Gunakan hooks routing
  // Kode kamu tidak pakai ini → tidak bisa tahu halaman aktif
  const location = useLocation()
  const navigate = useNavigate()
  const isLanding = location.pathname === '/'

  // ✅ PERBAIKAN 6: State untuk popup dan menu mobile
  // Kode kamu tidak punya state apapun
  const [popup, setPopup] = useState(null)
  const [mobileOpen, setMobileOpen] = useState(false)

  // ✅ PERBAIKAN 7: Logic navigasi cerdas
  // Kode kamu tidak punya fungsi ini sama sekali
  const handleNavClick = (type) => {
    setMobileOpen(false)
    if (isLanding) {
      // Jika di landing page → scroll ke section
      const id = type === 'cara-kerja' ? 'how-it-works' : 'features'
      const el = document.getElementById(id)
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' })
      } else {
        navigate('/')
        setTimeout(() => document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' }), 100)
      }
    } else {
      // Jika di halaman lain → buka popup
      setPopup(type)
    }
  }

  return (
    <>
      {/* ✅ PERBAIKAN 8: Navbar sticky dengan backdrop blur
          Kode kamu: bg-white dark:bg-gray-800 (solid, tidak blur)
          Perbaikan: bg-white/90 + backdrop-blur-md (transparan + blur) */}
      <nav className="sticky top-0 z-40 bg-white/90 dark:bg-gray-900/90 backdrop-blur-md border-b border-gray-200/50 dark:border-gray-700/50 transition-colors duration-300">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">

            {/* ✅ PERBAIKAN 9: Logo dibungkus Link dengan gradient & hover effect
                Kode kamu: <div> biasa tanpa Link, tanpa gradient */}
            <Link to="/" className="flex items-center gap-2 group flex-shrink-0">
              <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-lg group-hover:shadow-indigo-500/30 transition-shadow duration-200">
                <GraduationCap className="w-5 h-5 text-white" />
              </div>
              <span className="text-lg font-bold text-gray-900 dark:text-white">
                Acad<span className="text-indigo-600 dark:text-indigo-400">Predict</span>
              </span>
            </Link>

            {/* ✅ PERBAIKAN 10: Navigasi desktop (Beranda, Cara Kerja, Fitur)
                Kode kamu: TIDAK ADA navigasi sama sekali */}
            <div className="hidden md:flex items-center gap-6">
              <Link
                to="/"
                className={`text-sm font-medium transition-colors ${isLanding ? 'text-indigo-600 dark:text-indigo-400' : 'text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white'}`}
              >
                Beranda
              </Link>
              <button onClick={() => handleNavClick('cara-kerja')} className="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition-colors">
                Cara Kerja
              </button>
              <button onClick={() => handleNavClick('fitur')} className="text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white transition-colors">
                Fitur
              </button>
            </div>

            {/* Sisi kanan: Cari Mahasiswa + Dark Mode + Hamburger */}
            <div className="flex items-center gap-2">
              {/* ✅ PERBAIKAN 11: Tombol "Cari Mahasiswa" muncul saat bukan di landing
                  Kode kamu: TIDAK ADA */}
              {!isLanding && (
                <Link to="/" className="hidden sm:flex items-center gap-1.5 text-sm font-medium text-gray-600 dark:text-gray-300 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors px-3 py-1.5 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800">
                  <BarChart3 className="w-4 h-4" />
                  <span>Cari Mahasiswa</span>
                </Link>
              )}

              {/* ✅ Dark mode toggle (ada di kode kamu, tapi styling-nya sedikit berbeda)
                  Kode kamu: bg-gray-200 dark:bg-gray-700 hover:scale-105
                  Perbaikan: bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 (lebih halus) */}
              <button
                onClick={() => setDarkMode(!darkMode)}
                className="w-9 h-9 rounded-xl flex items-center justify-center bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors duration-200"
                aria-label="Toggle dark mode"
              >
                {darkMode ? <Sun className="w-4 h-4" /> : <Moon className="w-4 h-4" />}
              </button>

              {/* ✅ PERBAIKAN 12: Tombol hamburger untuk menu mobile
                  Kode kamu: TIDAK ADA */}
              <button
                onClick={() => setMobileOpen(!mobileOpen)}
                className="md:hidden w-9 h-9 rounded-xl flex items-center justify-center bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
                aria-label="Toggle menu"
              >
                {mobileOpen ? <X className="w-4 h-4" /> : <Menu className="w-4 h-4" />}
              </button>
            </div>
          </div>
        </div>

        {/* ✅ PERBAIKAN 13: Menu mobile dropdown
            Kode kamu: TIDAK ADA menu mobile sama sekali */}
        {mobileOpen && (
          <div className="md:hidden border-t border-gray-100 dark:border-gray-800 bg-white dark:bg-gray-900 px-4 py-3 space-y-1 animate-fade-in">
            <Link
              to="/"
              onClick={() => setMobileOpen(false)}
              className="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            >
              <Home className="w-4 h-4 text-indigo-500" />
              Beranda
            </Link>
            <button
              onClick={() => handleNavClick('cara-kerja')}
              className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-left"
            >
              <Cpu className="w-4 h-4 text-indigo-500" />
              Cara Kerja
            </button>
            <button
              onClick={() => handleNavClick('fitur')}
              className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors text-left"
            >
              <Zap className="w-4 h-4 text-indigo-500" />
              Fitur
            </button>
            {!isLanding && (
              <Link
                to="/"
                onClick={() => setMobileOpen(false)}
                className="flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-indigo-600 dark:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-indigo-900/20 transition-colors"
              >
                <BarChart3 className="w-4 h-4" />
                Cari Mahasiswa
              </Link>
            )}
          </div>
        )}
      </nav>

      {/* ✅ PERBAIKAN 14: Render popup jika ada yang aktif
          Kode kamu: TIDAK ADA */}
      {popup && <NavPopup type={popup} onClose={() => setPopup(null)} />}
    </>
  )
}
