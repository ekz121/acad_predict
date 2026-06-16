import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8001'

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 15000,
  headers: {
    'Content-Type': 'application/json',
  },
})

api.interceptors.response.use(
  (response) => response.data,
  (error) => {
    const message =
      error.response?.data?.detail ||
      error.response?.data?.message ||
      error.message ||
      'Terjadi kesalahan pada server.'
    return Promise.reject(new Error(message))
  }
)

export const getStudent = (nim) => api.get(`/api/student/${nim}`)
export const getPredict = (nim) => api.get(`/api/predict/${nim}`)
export const getStudents = (params = {}) => api.get('/api/students', { params })
export const getHealth = () => api.get('/health')
export const postIPKTarget = (nim, payload) => api.post(`/api/ipk-target/${nim}`, payload)

export default api
