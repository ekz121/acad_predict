import { useState, useRef, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Search, ArrowRight, Brain, BarChart3, BookOpen, Users,
  Zap, TrendingUp, GraduationCap, Star,
  ChevronRight, Cpu, Database, Layers,
  Monitor, Calculator, Settings, FileText
} from 'lucide-react'

import { InlineSpinner } from '../components/LoadingSpinner'
import { getStudent } from '../api/client'

// ─────────────────────────────────────────────
// DATA
// ─────────────────────────────────────────────
const PRODI_LIST = [
  { name: 'Teknologi Informasi', key: 'TI', color: 'from-indigo-400 to-blue-500', icon: Monitor, desc: 'Rekayasa perangkat lunak, jaringan, dan kecerdasan buatan' },
  { name: 'Akuntansi', key: 'AK', color: 'from-emerald-400 to-teal-500', icon: Calculator, desc: 'Keuangan, perpajakan, auditing, dan sistem informasi akuntansi' },
  { name: 'Teknik Mesin', key: 'TM', color: 'from-orange-400 to-red-500', icon: Settings, desc: 'Manufaktur, termodinamika, dan perancangan mesin industri' },
  { name: 'Administrasi Perkantoran', key: 'AP', color: 'from-violet-400 to-purple-500', icon: FileText, desc: 'Manajemen perkantoran, sekretaris, dan digitalisasi bisnis' },
]

const FEATURES = [
  { icon: Brain, title: 'Prediksi Berbasis AI', desc: 'Algoritma prediksi berbasis data historis dengan weighted average dan analisis tren semester.', color: 'from-indigo-500 to-blue-600' },
  { icon: BarChart3, title: 'Visualisasi Tren IPK', desc: 'Grafik interaktif menampilkan tren performa akademik dari semester ke semester.', color: 'from-purple-500 to-pink-600' },
  { icon: BookOpen, title: 'Prediksi Per Mata Kuliah', desc: 'Prediksi nilai untuk setiap mata kuliah semester berikutnya beserta tingkat kepercayaan.', color: 'from-emerald-500 to-teal-600' },
  { icon: Zap, title: 'Simulasi Beban SKS', desc: 'Simulasi 4 skenario SKS dengan prediksi IPS dan IPK untuk setiap pilihan.', color: 'from-amber-500 to-orange-600' },
]

const HOW_IT_WORKS = [
  { step: '01', title: 'Masukkan NIM', desc: 'Masukkan NIM 8 digit mahasiswa.', icon: Search },
  { step: '02', title: 'Analisis Data Historis', desc: 'Sistem menganalisis nilai dari semua semester.', icon: Database },
  { step: '03', title: 'Kalkulasi Prediksi', desc: 'Algoritma weighted average menghitung prediksi.', icon: Cpu },
  { step: '04', title: 'Tampilkan Dashboard', desc: 'Hasil ditampilkan dalam dashboard.', icon: Layers },
]

// ─────────────────────────────────────────────
// VALIDATION
// ─────────────────────────────────────────────
function validateNIM(nim) {
  if (!/^\d{8}$/.test(nim)) return 'NIM harus terdiri dari 8 digit angka.'
  return null
}

// ─────────────────────────────────────────────
// COMPONENT
// ─────────────────────────────────────────────
export default function Landing() {
  const [nim, setNim] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const navigate = useNavigate()
  const searchRef = useRef(null)
  const isMounted = useRef(true)

  // cleanup
 import { useState, useRef, useCallback, useEffect } from 'react'
 useEffect(() => {
  return () => {
    isMounted.current = false
  }
}, [])

  const handleSearch = useCallback(async (searchNim = nim) => {
    const trimmed = searchNim.trim()

    const validationError = validateNIM(trimmed)
    if (validationError) {
      setError(validationError)
      return
    }

    setError('')
    setLoading(true)

    try {
      await getStudent(trimmed)

      if (!isMounted.current) return
      navigate(`/dashboard/${trimmed}`)

    } catch (err) {
      if (!isMounted.current) return

      setError(
        err?.message ||
        err?.response?.data?.message ||
        'Mahasiswa tidak ditemukan.'
      )
    } finally {
      if (isMounted.current) {
        setLoading(false)
      }
    }
  }, [nim, navigate])

  return (
    <div className="min-h-screen">

      {/* HERO */}
      <section className="pt-16 pb-20 text-center">
        <h1 className="text-4xl font-extrabold mb-4">
          Prediksi Masa Depan Akademikmu
        </h1>

        <div ref={searchRef} className="max-w-md mx-auto mt-6">
          <div className="flex gap-2">
            <input
              type="text"
              value={nim}
              maxLength={8}
              disabled={loading}
              onChange={(e) => {
                setNim(e.target.value)
                setError('')
              }}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
              placeholder="Masukkan NIM"
              className="flex-1 border px-3 py-2 rounded-lg"
            />

            <button
              onClick={() => handleSearch()}
              disabled={loading}
              className="px-4 py-2 bg-indigo-600 text-white rounded-lg flex items-center gap-2"
            >
              {loading ? <InlineSpinner /> : 'Cari'}
              {!loading && <ArrowRight size={16} />}
            </button>
          </div>

          {error && (
            <p className="text-red-500 text-sm mt-2">
              {error}
            </p>
          )}
        </div>
      </section>

      {/* FOOTER */}
      <footer className="text-center py-6 text-sm text-gray-500">
        AcadPredict © 2026
      </footer>
    </div>
  )
}
