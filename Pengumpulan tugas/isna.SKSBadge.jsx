import React, { useState } from 'react';
import './SKSBadge.css';

const SKSBadge = ({ sksData = [] }) => {
  const [filterStatus, setFilterStatus] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortConfig, setSortConfig] = useState(null);

  // Filter and search data
  let filteredData = sksData;

  if (filterStatus !== 'all') {
    filteredData = filteredData.filter((item) => item.status === filterStatus);
  }

  if (searchTerm) {
    filteredData = filteredData.filter((item) =>
      item.studentName?.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.courseName?.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }

  // Handle sorting
  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig && sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });

    const sorted = [...filteredData].sort((a, b) => {
      const aValue = a[key];
      const bValue = b[key];

      if (typeof aValue === 'number' && typeof bValue === 'number') {
        return direction === 'asc' ? aValue - bValue : bValue - aValue;
      }

      if (aValue < bValue) return direction === 'asc' ? -1 : 1;
      if (aValue > bValue) return direction === 'asc' ? 1 : -1;
      return 0;
    });
    filteredData = sorted;
  };

  // Get status badge class
  const getStatusClass = (status) => {
    switch (status) {
      case 'Lulus':
        return 'badge-success';
      case 'Dalam Proses':
        return 'badge-warning';
      case 'Tidak Lulus':
        return 'badge-danger';
      default:
        return 'badge-default';
    }
  };

  // Get status icon
  const getStatusIcon = (status) => {
    switch (status) {
      case 'Lulus':
        return '✓';
      case 'Dalam Proses':
        return '⟳';
      case 'Tidak Lulus':
        return '✕';
      default:
        return '○';
    }
  };

  // Calculate statistics
  const totalSKS = filteredData.reduce((sum, item) => sum + item.sks, 0);
  const totalCourses = filteredData.length;
  const passedCourses = filteredData.filter((item) => item.status === 'Lulus').length;
  const passingPercentage = totalCourses > 0 ? ((passedCourses / totalCourses) * 100).toFixed(1) : 0;

  return (
    <div className="sks-badge-container">
      <div className="header-section">
        <h2>Badge SKS Siswa</h2>
        <p>Sistem Kredit Semester</p>
      </div>

      <div className="controls-section">
        <div className="search-group">
          <input
            type="text"
            placeholder="Cari nama siswa atau course..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>

        <div className="filter-group">
          <label htmlFor="status">Filter Status:</label>
          <select
            id="status"
            value={filterStatus}
            onChange={(e) => setFilterStatus(e.target.value)}
            className="select-input"
          >
            <option value="all">Semua Status</option>
            <option value="Lulus">Lulus</option>
            <option value="Dalam Proses">Dalam Proses</option>
            <option value="Tidak Lulus">Tidak Lulus</option>
          </select>
        </div>
      </div>

      <div className="stats-section">
        <div className="stat-card">
          <span className="stat-label">Total SKS</span>
          <span className="stat-value">{totalSKS}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Total Course</span>
          <span className="stat-value">{totalCourses}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Course Lulus</span>
          <span className="stat-value">{passedCourses}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Persentase Lulus</span>
          <span className="stat-value">{passingPercentage}%</span>
        </div>
      </div>

      <div className="badges-section">
        <h3>Daftar Badge SKS</h3>
        {filteredData.length > 0 ? (
          <div className="badges-grid">
            {filteredData.map((item) => (
              <div key={item.id} className={`badge-card ${getStatusClass(item.status)}`}>
                <div className="badge-header">
                  <div className="badge-status-icon">
                    {getStatusIcon(item.status)}
                  </div>
                  <span className="badge-status">{item.status}</span>
                </div>

                <div className="badge-content">
                  <div className="badge-info">
                    <p className="course-name">{item.courseName}</p>
                    <p className="student-name">{item.studentName}</p>
                  </div>

                  <div className="badge-details">
                    <div className="detail-item">
                      <span className="detail-label">SKS:</span>
                      <span className="detail-value">{item.sks}</span>
                    </div>
                    <div className="detail-item">
                      <span className="detail-label">Nilai:</span>
                      <span className="detail-value">{item.grade}</span>
                    </div>
                  </div>

                  <div className="badge-footer">
                    <span className="semester">Semester {item.semester}</span>
                    <span className="date">
                      {new Date(item.completionDate).toLocaleDateString('id-ID')}
                    </span>
                  </div>
                </div>

                <div className="badge-actions">
                  <button className="btn btn-view" title="Lihat Detail">Lihat</button>
                  <button className="btn btn-edit" title="Edit">Edit</button>
                  <button className="btn btn-delete" title="Hapus">Hapus</button>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="no-data">
            Tidak ada data SKS untuk ditampilkan
          </div>
        )}
      </div>

      <div className="legend-section">
        <h3>Keterangan Status</h3>
        <div className="legend-items">
          <div className="legend-item">
            <div className="legend-badge badge-success">✓</div>
            <span>Lulus - Siswa telah menyelesaikan course dengan nilai memuaskan</span>
          </div>
          <div className="legend-item">
            <div className="legend-badge badge-warning">⟳</div>
            <span>Dalam Proses - Siswa masih mengikuti course</span>
          </div>
          <div className="legend-item">
            <div className="legend-badge badge-danger">✕</div>
            <span>Tidak Lulus - Siswa belum mencapai nilai minimum</span>
          </div>
        </div>
      </div>

      <div className="info-section">
        <h3>Informasi</h3>
        <p>
          SKS (Sistem Kredit Semester) adalah satuan besaran program pendidikan yang mengukur beban studi siswa,
          beban mengajar dosen, dan beban kerja dosen lain dalam suatu program pendidikan.
        </p>
      </div>
    </div>
  );
};

export default SKSBadge;
