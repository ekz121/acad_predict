import React, { useState } from 'react';
import {
  BarChart,
  Bar,
  LineChart,
  Line,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import './IPKChart.css';

const IPKChart = ({ ipkData = [] }) => {
  const [chartType, setChartType] = useState('bar');
  const [selectedSemester, setSelectedSemester] = useState('all');

  // Get unique semesters
  const semesters = ['all', ...new Set(ipkData.map((item) => item.semester))].sort();

  // Filter data based on selected semester
  const filteredData = selectedSemester === 'all'
    ? ipkData
    : ipkData.filter((item) => item.semester === parseInt(selectedSemester));

  // Prepare data for charts
  const chartData = filteredData.map((item) => ({
    name: item.studentName,
    ipk: parseFloat(item.ipk),
    semester: item.semester,
  }));

  // Prepare pie chart data
  const pieData = [
    {
      name: 'IPK >= 3.5',
      value: filteredData.filter((item) => item.ipk >= 3.5).length,
      color: '#10B981',
    },
    {
      name: 'IPK 3.0 - 3.5',
      value: filteredData.filter((item) => item.ipk >= 3.0 && item.ipk < 3.5).length,
      color: '#3B82F6',
    },
    {
      name: 'IPK 2.5 - 3.0',
      value: filteredData.filter((item) => item.ipk >= 2.5 && item.ipk < 3.0).length,
      color: '#F59E0B',
    },
    {
      name: 'IPK < 2.5',
      value: filteredData.filter((item) => item.ipk < 2.5).length,
      color: '#EF4444',
    },
  ];

  // Calculate statistics
  const avgIPK = filteredData.length > 0
    ? (filteredData.reduce((sum, item) => sum + item.ipk, 0) / filteredData.length).toFixed(2)
    : 0;

  const maxIPK = filteredData.length > 0
    ? Math.max(...filteredData.map((item) => item.ipk)).toFixed(2)
    : 0;

  const minIPK = filteredData.length > 0
    ? Math.min(...filteredData.map((item) => item.ipk)).toFixed(2)
    : 0;

  const totalStudents = filteredData.length;

  return (
    <div className="ipk-chart-container">
      <div className="header-section">
        <h2>Grafik IPK Siswa</h2>
      </div>

      <div className="controls-section">
        <div className="filter-group">
          <label htmlFor="semester">Pilih Semester:</label>
          <select
            id="semester"
            value={selectedSemester}
            onChange={(e) => setSelectedSemester(e.target.value)}
            className="select-input"
          >
            <option value="all">Semua Semester</option>
            {semesters.filter((s) => s !== 'all').map((semester) => (
              <option key={semester} value={semester}>
                Semester {semester}
              </option>
            ))}
          </select>
        </div>

        <div className="chart-type-group">
          <label>Tipe Grafik:</label>
          <button
            className={`chart-btn ${chartType === 'bar' ? 'active' : ''}`}
            onClick={() => setChartType('bar')}
          >
            Bar Chart
          </button>
          <button
            className={`chart-btn ${chartType === 'line' ? 'active' : ''}`}
            onClick={() => setChartType('line')}
          >
            Line Chart
          </button>
          <button
            className={`chart-btn ${chartType === 'pie' ? 'active' : ''}`}
            onClick={() => setChartType('pie')}
          >
            Pie Chart
          </button>
        </div>
      </div>

      <div className="stats-section">
        <div className="stat-card">
          <span className="stat-label">Rata-rata IPK</span>
          <span className="stat-value">{avgIPK}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">IPK Tertinggi</span>
          <span className="stat-value">{maxIPK}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">IPK Terendah</span>
          <span className="stat-value">{minIPK}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Total Siswa</span>
          <span className="stat-value">{totalStudents}</span>
        </div>
      </div>

      <div className="chart-section">
        {chartData.length > 0 ? (
          <>
            {chartType === 'bar' && (
              <ResponsiveContainer width="100%" height={400}>
                <BarChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
                  <YAxis domain={[0, 4]} />
                  <Tooltip />
                  <Legend />
                  <Bar dataKey="ipk" fill="#3B82F6" name="IPK" />
                </BarChart>
              </ResponsiveContainer>
            )}

            {chartType === 'line' && (
              <ResponsiveContainer width="100%" height={400}>
                <LineChart data={chartData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
                  <YAxis domain={[0, 4]} />
                  <Tooltip />
                  <Legend />
                  <Line
                    type="monotone"
                    dataKey="ipk"
                    stroke="#10B981"
                    name="IPK"
                    dot={{ fill: '#10B981', r: 5 }}
                    activeDot={{ r: 7 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            )}

            {chartType === 'pie' && (
              <ResponsiveContainer width="100%" height={400}>
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, value }) => `${name}: ${value}`}
                    outerRadius={120}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {pieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            )}
          </>
        ) : (
          <div className="no-data">Tidak ada data IPK untuk ditampilkan</div>
        )}
      </div>

      <div className="legend-section">
        <h3>Keterangan Kategori IPK</h3>
        <div className="legend-items">
          <div className="legend-item">
            <div className="legend-color" style={{ backgroundColor: '#10B981' }}></div>
            <span>IPK >= 3.5 (Sangat Baik)</span>
          </div>
          <div className="legend-item">
            <div className="legend-color" style={{ backgroundColor: '#3B82F6' }}></div>
            <span>IPK 3.0 - 3.5 (Baik)</span>
          </div>
          <div className="legend-item">
            <div className="legend-color" style={{ backgroundColor: '#F59E0B' }}></div>
            <span>IPK 2.5 - 3.0 (Cukup)</span>
          </div>
          <div className="legend-item">
            <div className="legend-color" style={{ backgroundColor: '#EF4444' }}></div>
            <span>IPK < 2.5 (Kurang)</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default IPKChart;
