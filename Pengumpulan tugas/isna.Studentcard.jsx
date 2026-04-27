import React, { useState } from 'react';
import './StudentCard.css';

const StudentCard = ({ students = [] }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterStatus, setFilterStatus] = useState('all');
  const [sortBy, setSortBy] = useState('name');
  const [viewMode, setViewMode] = useState('grid');

  // Filter and search data
  let filteredStudents = students;

  if (searchTerm) {
    filteredStudents = filteredStudents.filter((student) =>
      student.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      student.studentId?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      student.email?.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }

  if (filterStatus !== 'all') {
    filteredStudents = filteredStudents.filter((student) => student.status === filterStatus);
  }

  // Handle sorting
  if (sortBy === 'name') {
    filteredStudents.sort((a, b) => a.name.localeCompare(b.name));
  } else if (sortBy === 'ipk') {
    filteredStudents.sort((a, b) => b.ipk - a.ipk);
  } else if (sortBy === 'sks') {
    filteredStudents.sort((a, b) => b.totalSKS - a.totalSKS);
  }

  // Get status badge class
  const getStatusClass = (status) => {
    switch (status) {
      case 'Aktif':
        return 'status-active';
      case 'Cuti':
        return 'status-leave';
      case 'Non-Aktif':
        return 'status-inactive';
      default:
        return 'status-default';
    }
  };

  // Get status icon
  const getStatusIcon = (status) => {
    switch (status) {
      case 'Aktif':
        return '●';
      case 'Cuti':
        return '⊘';
      case 'Non-Aktif':
        return '○';
      default:
        return '?';
    }
  };

  // Get IPK category
  const getIPKCategory = (ipk) => {
    if (ipk >= 3.5) return 'Sangat Baik';
    if (ipk >= 3.0) return 'Baik';
    if (ipk >= 2.5) return 'Cukup';
    return 'Kurang';
  };

  // Get IPK color class
  const getIPKColorClass = (ipk) => {
    if (ipk >= 3.5) return 'ipk-excellent';
    if (ipk >= 3.0) return 'ipk-good';
    if (ipk >= 2.5) return 'ipk-fair';
    return 'ipk-poor';
  };

  // Statistics
  const totalStudents = students.length;
  const activeStudents = students.filter((s) => s.status === 'Aktif').length;
  const averageIPK = students.length > 0
    ? (students.reduce((sum, s) => sum + s.ipk, 0) / students.length).toFixed(2)
    : 0;

  return (
    <div className="student-card-container">
      <div className="header-section">
        <h2>Kartu Siswa</h2>
        <p>Manajemen Data Siswa</p>
      </div>

      <div className="stats-bar">
        <div className="stat-item">
          <span className="stat-label">Total Siswa</span>
          <span className="stat-value">{totalStudents}</span>
        </div>
        <div className="stat-item">
          <span className="stat-label">Siswa Aktif</span>
          <span className="stat-value">{activeStudents}</span>
        </div>
        <div className="stat-item">
          <span className="stat-label">Rata-rata IPK</span>
          <span className="stat-value">{averageIPK}</span>
        </div>
      </div>

      <div className="controls-section">
        <div className="search-group">
          <input
            type="text"
            placeholder="Cari nama, NIM, atau email..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>

        <div className="filters-group">
          <div className="filter-item">
            <label htmlFor="status">Status:</label>
            <select
              id="status"
              value={filterStatus}
              onChange={(e) => setFilterStatus(e.target.value)}
              className="select-input"
            >
              <option value="all">Semua Status</option>
              <option value="Aktif">Aktif</option>
              <option value="Cuti">Cuti</option>
              <option value="Non-Aktif">Non-Aktif</option>
            </select>
          </div>

          <div className="filter-item">
            <label htmlFor="sortby">Urutkan:</label>
            <select
              id="sortby"
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="select-input"
            >
              <option value="name">Nama (A-Z)</option>
              <option value="ipk">IPK (Tertinggi)</option>
              <option value="sks">SKS (Terbanyak)</option>
            </select>
          </div>

          <div className="view-mode-group">
            <button
              className={`view-btn ${viewMode === 'grid' ? 'active' : ''}`}
              onClick={() => setViewMode('grid')}
              title="Grid View"
            >
              ⊞
            </button>
            <button
              className={`view-btn ${viewMode === 'list' ? 'active' : ''}`}
              onClick={() => setViewMode('list')}
              title="List View"
            >
              ≡
            </button>
          </div>
        </div>
      </div>

      {filteredStudents.length > 0 ? (
        <>
          {viewMode === 'grid' && (
            <div className="cards-grid">
              {filteredStudents.map((student) => (
                <div key={student.id} className={`student-card ${getStatusClass(student.status)}`}>
                  <div className="card-header">
                    <div className="student-avatar">
                      {student.avatar ? (
                        <img src={student.avatar} alt={student.name} />
                      ) : (
                        <div className="avatar-placeholder">
                          {student.name.charAt(0).toUpperCase()}
                        </div>
                      )}
                    </div>
                    <div className="status-badge">
                      <span className={`badge ${getStatusClass(student.status)}`}>
                        {getStatusIcon(student.status)} {student.status}
                      </span>
                    </div>
                  </div>

                  <div className="card-body">
                    <h3 className="student-name">{student.name}</h3>
                    <p className="student-id">NIM: {student.studentId}</p>
                    <p className="student-email">{student.email}</p>

                    <div className="card-details">
                      <div className="detail-row">
                        <span className="detail-label">Program Studi:</span>
                        <span className="detail-value">{student.program}</span>
                      </div>
                      <div className="detail-row">
                        <span className="detail-label">Semester:</span>
                        <span className="detail-value">{student.semester}</span>
                      </div>
                      <div className="detail-row">
                        <span className="detail-label">Angkatan:</span>
                        <span className="detail-value">{student.cohort}</span>
                      </div>
                    </div>

                    <div className="card-metrics">
                      <div className="metric-item">
                        <span className="metric-label">IPK</span>
                        <span className={`metric-value ${getIPKColorClass(student.ipk)}`}>
                          {student.ipk}
                        </span>
                        <span className="metric-category">{getIPKCategory(student.ipk)}</span>
                      </div>
                      <div className="metric-item">
                        <span className="metric-label">SKS</span>
                        <span className="metric-value">{student.totalSKS}</span>
                      </div>
                      <div className="metric-item">
                        <span className="metric-label">Nilai Rata-rata</span>
                        <span className="metric-value">{student.averageGrade}</span>
                      </div>
                    </div>
                  </div>

                  <div className="card-footer">
                    <button className="btn btn-view">Profil</button>
                    <button className="btn btn-edit">Edit</button>
                    <button className="btn btn-delete">Hapus</button>
                  </div>
                </div>
              ))}
            </div>
          )}

          {viewMode === 'list' && (
            <div className="cards-list">
              <div className="list-header">
                <div className="col col-name">Nama</div>
                <div className="col col-id">NIM</div>
                <div className="col col-program">Program Studi</div>
                <div className="col col-semester">Semester</div>
                <div className="col col-ipk">IPK</div>
                <div className="col col-status">Status</div>
                <div className="col col-actions">Aksi</div>
              </div>
              {filteredStudents.map((student) => (
                <div key={student.id} className={`list-row ${getStatusClass(student.status)}`}>
                  <div className="col col-name">
                    <div className="name-with-avatar">
                      <div className="small-avatar">
                        {student.avatar ? (
                          <img src={student.avatar} alt={student.name} />
                        ) : (
                          student.name.charAt(0).toUpperCase()
                        )}
                      </div>
                      <span>{student.name}</span>
                    </div>
                  </div>
                  <div className="col col-id">{student.studentId}</div>
                  <div className="col col-program">{student.program}</div>
                  <div className="col col-semester">{student.semester}</div>
                  <div className={`col col-ipk ${getIPKColorClass(student.ipk)}`}>
                    {student.ipk}
                  </div>
                  <div className="col col-status">
                    <span className={`status-badge ${getStatusClass(student.status)}`}>
                      {getStatusIcon(student.status)} {student.status}
                    </span>
                  </div>
                  <div className="col col-actions">
                    <button className="btn btn-sm btn-view">Profil</button>
                    <button className="btn btn-sm btn-edit">Edit</button>
                    <button className="btn btn-sm btn-delete">Hapus</button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </>
      ) : (
        <div className="no-data">
          Tidak ada data siswa untuk ditampilkan
        </div>
      )}

      <div className="legend-section">
        <h3>Keterangan Status</h3>
        <div className="legend-items">
          <div className="legend-item">
            <span className="legend-status status-active">●</span>
            <span>Aktif - Siswa sedang melakukan perkuliahan</span>
          </div>
          <div className="legend-item">
            <span className="legend-status status-leave">⊘</span>
            <span>Cuti - Siswa sedang mengambil cuti akademik</span>
          </div>
          <div className="legend-item">
            <span className="legend-status status-inactive">○</span>
            <span>Non-Aktif - Siswa tidak lagi terdaftar</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentCard;
