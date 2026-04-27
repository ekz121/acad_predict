import React, { useState } from 'react';
import './GradeHistoryTable.css';

const GradeHistoryTable = ({ grades = [] }) => {
  const [sortConfig, setSortConfig] = useState(null);
  const [filteredGrades, setFilteredGrades] = useState(grades);
  const [searchTerm, setSearchTerm] = useState('');

  // Handle sorting
  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig && sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });

    const sorted = [...filteredGrades].sort((a, b) => {
      const aValue = a[key];
      const bValue = b[key];

      if (typeof aValue === 'number' && typeof bValue === 'number') {
        return direction === 'asc' ? aValue - bValue : bValue - aValue;
      }

      if (aValue < bValue) return direction === 'asc' ? -1 : 1;
      if (aValue > bValue) return direction === 'asc' ? 1 : -1;
      return 0;
    });
    setFilteredGrades(sorted);
  };

  // Handle search filter
  const handleSearch = (e) => {
    const term = e.target.value.toLowerCase();
    setSearchTerm(term);

    const filtered = grades.filter((grade) =>
      grade.studentName?.toLowerCase().includes(term) ||
      grade.courseName?.toLowerCase().includes(term)
    );
    setFilteredGrades(filtered);
  };

  // Get grade status (Passed/Failed)
  const getGradeStatus = (score) => {
    return score >= 60 ? 'Lulus' : 'Tidak Lulus';
  };

  // Get grade status class
  const getStatusClass = (score) => {
    return score >= 60 ? 'status-pass' : 'status-fail';
  };

  // Get letter grade
  const getLetterGrade = (score) => {
    if (score >= 85) return 'A';
    if (score >= 75) return 'B';
    if (score >= 65) return 'C';
    if (score >= 60) return 'D';
    return 'E';
  };

  return (
    <div className="grade-history-container">
      <div className="header-section">
        <h2>Riwayat Nilai</h2>
        <div className="search-bar">
          <input
            type="text"
            placeholder="Cari nama siswa atau nama course..."
            value={searchTerm}
            onChange={handleSearch}
            className="search-input"
          />
        </div>
      </div>

      <div className="table-wrapper">
        <table className="grade-table">
          <thead>
            <tr>
              <th onClick={() => handleSort('id')}>
                ID {sortConfig?.key === 'id' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
              </th>
              <th onClick={() => handleSort('studentName')}>
                Nama Siswa {sortConfig?.key === 'studentName' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
              </th>
              <th onClick={() => handleSort('courseName')}>
                Nama Course {sortConfig?.key === 'courseName' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
              </th>
              <th onClick={() => handleSort('score')}>
                Nilai {sortConfig?.key === 'score' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
              </th>
              <th>Grade</th>
              <th>Status</th>
              <th onClick={() => handleSort('date')}>
                Tanggal {sortConfig?.key === 'date' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
              </th>
              <th>Aksi</th>
            </tr>
          </thead>
          <tbody>
            {filteredGrades.length > 0 ? (
              filteredGrades.map((grade) => (
                <tr key={grade.id}>
                  <td>{grade.id}</td>
                  <td>{grade.studentName}</td>
                  <td>{grade.courseName}</td>
                  <td className="score-cell">{grade.score}</td>
                  <td className="grade-cell">{getLetterGrade(grade.score)}</td>
                  <td>
                    <span className={`status-badge ${getStatusClass(grade.score)}`}>
                      {getGradeStatus(grade.score)}
                    </span>
                  </td>
                  <td>{new Date(grade.date).toLocaleDateString('id-ID')}</td>
                  <td>
                    <button className="btn btn-view">Lihat</button>
                    <button className="btn btn-edit">Edit</button>
                    <button className="btn btn-delete">Hapus</button>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="8" className="no-data">
                  Tidak ada data riwayat nilai
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {filteredGrades.length > 0 && (
        <div className="stats-section">
          <div className="stat">
            <span className="stat-label">Total Nilai:</span>
            <span className="stat-value">{filteredGrades.length}</span>
          </div>
          <div className="stat">
            <span className="stat-label">Rata-rata Nilai:</span>
            <span className="stat-value">
              {(filteredGrades.reduce((sum, g) => sum + g.score, 0) / filteredGrades.length).toFixed(2)}
            </span>
          </div>
          <div className="stat">
            <span className="stat-label">Nilai Tertinggi:</span>
            <span className="stat-value">{Math.max(...filteredGrades.map(g => g.score))}</span>
          </div>
          <div className="stat">
            <span className="stat-label">Nilai Terendah:</span>
            <span className="stat-value">{Math.min(...filteredGrades.map(g => g.score))}</span>
          </div>
        </div>
      )}
    </div>
  );
};

export default GradeHistoryTable;
