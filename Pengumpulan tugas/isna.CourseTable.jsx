import React, { useState } from 'react';
import './CourseTable.css';

const CourseTable = ({ courses = [] }) => {
  const [sortConfig, setSortConfig] = useState(null);
  const [filteredCourses, setFilteredCourses] = useState(courses);

  // Handle sorting
  const handleSort = (key) => {
    let direction = 'asc';
    if (sortConfig && sortConfig.key === key && sortConfig.direction === 'asc') {
      direction = 'desc';
    }
    setSortConfig({ key, direction });

    const sorted = [...filteredCourses].sort((a, b) => {
      if (a[key] < b[key]) return direction === 'asc' ? -1 : 1;
      if (a[key] > b[key]) return direction === 'asc' ? 1 : -1;
      return 0;
    });
    setFilteredCourses(sorted);
  };

  // Handle search filter
  const handleSearch = (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const filtered = courses.filter((course) =>
      course.name?.toLowerCase().includes(searchTerm) ||
      course.instructor?.toLowerCase().includes(searchTerm)
    );
    setFilteredCourses(filtered);
  };

  return (
    <div className="course-table-container">
      <div className="search-bar">
        <input
          type="text"
          placeholder="Cari course atau instructor..."
          onChange={handleSearch}
          className="search-input"
        />
      </div>

      <table className="course-table">
        <thead>
          <tr>
            <th onClick={() => handleSort('id')}>
              ID {sortConfig?.key === 'id' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
            </th>
            <th onClick={() => handleSort('name')}>
              Nama Course {sortConfig?.key === 'name' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
            </th>
            <th onClick={() => handleSort('instructor')}>
              Instruktur {sortConfig?.key === 'instructor' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
            </th>
            <th onClick={() => handleSort('students')}>
              Jumlah Siswa {sortConfig?.key === 'students' && (sortConfig.direction === 'asc' ? '↑' : '↓')}
            </th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          {filteredCourses.length > 0 ? (
            filteredCourses.map((course) => (
              <tr key={course.id}>
                <td>{course.id}</td>
                <td>{course.name}</td>
                <td>{course.instructor}</td>
                <td>{course.students}</td>
                <td>
                  <button className="btn btn-view">Lihat</button>
                  <button className="btn btn-edit">Edit</button>
                  <button className="btn btn-delete">Hapus</button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5" className="no-data">
                Tidak ada data course
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default CourseTable;
