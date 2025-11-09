import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
  BarChart,
  Bar,
  CartesianGrid,
} from "recharts";
import "./App.css";

function App() {
  const [vitals, setVitals] = useState(null);
  const [history, setHistory] = useState([]);
  const [riskSummary, setRiskSummary] = useState({ Normal: 0, Moderate: 0, High: 0 });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const res = await fetch("http://127.0.0.1:5000/api/vitals");
        const data = await res.json();
        setVitals(data);

        const newEntry = {
          time: new Date().toLocaleTimeString(),
          heart_rate_bpm: data.heart_rate_bpm,
          spo2_percent: data.spo2_percent,
          body_temperature_c: data.body_temperature_c,
          risk_level: data.risk_level,
        };

        setHistory((prev) => [newEntry, ...prev.slice(0, 19)]);

        // Update risk summary counts
        setRiskSummary((prev) => ({
          ...prev,
          [data.risk_level]: (prev[data.risk_level] || 0) + 1,
        }));
      } catch {
        console.error("❌ API Fetch Error");
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 5000);
    return () => clearInterval(interval);
  }, []);

  if (!vitals)
    return (
      <div className="loading-screen">
        <h2>🧠 Real-time Epileptic Seizure Monitoring</h2>
        <p>Loading live data...</p>
      </div>
    );

  const getRiskColor = (risk) => {
    switch (risk) {
      case "High":
        return "#ff4d4d";
      case "Moderate":
        return "#ffb84d";
      default:
        return "#5cd65c";
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1>🧠 Real-time Epileptic Seizure Monitoring</h1>
        <h3>
          Patient: <span className="highlight">{vitals.patient_id}</span>
        </h3>
      </header>

      {/* Vitals Display */}
      <section
        className="vitals-card"
        style={{ borderColor: getRiskColor(vitals.risk_level) }}
      >
        <div className="vitals-grid">
          <p>❤️ <strong>Heart Rate:</strong> {vitals.heart_rate_bpm} bpm</p>
          <p>🫁 <strong>SpO₂:</strong> {vitals.spo2_percent?.toFixed(1)}%</p>
          <p>🌡️ <strong>Temperature:</strong> {vitals.body_temperature_c?.toFixed(1)} °C</p>
          <p>🦶 <strong>Movement:</strong> {vitals.movement_g?.toFixed(2)} g</p>
          <p>😤 <strong>Stress Level:</strong> {vitals.stress_level}</p>
          <p>🍬 <strong>Blood Glucose:</strong> {vitals.blood_glucose_mgdl} mg/dL</p>
          <p>💤 <strong>Sleep Hours:</strong> {vitals.sleep_hours?.toFixed(1)} hrs</p>
          <p>🔊 <strong>Noise Exposure:</strong> {vitals.noise_exposure_db?.toFixed(1)} dB</p>
          <p>💡 <strong>Light:</strong> {vitals.ambient_light_lux?.toFixed(1)} lux</p>
        </div>

        <div
          className="risk-box"
          style={{
            backgroundColor: getRiskColor(vitals.risk_level),
          }}
        >
          <strong>Risk Level: {vitals.risk_level}</strong>
        </div>
      </section>

      {/* Charts Section */}
      <section className="chart-section">
        <h3>📈 Vital Trends (Last 20 Readings)</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={history.slice().reverse()}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="time" hide />
            <YAxis />
            <Tooltip />
            <Legend />
            <Line type="monotone" dataKey="heart_rate_bpm" stroke="#ff4d4d" name="Heart Rate" />
            <Line type="monotone" dataKey="spo2_percent" stroke="#0078ff" name="SpO₂ (%)" />
            <Line type="monotone" dataKey="body_temperature_c" stroke="#ffa31a" name="Temp (°C)" />
          </LineChart>
        </ResponsiveContainer>
      </section>

      {/* Risk Distribution */}
      <section className="chart-section">
        <h3>⚠️ Risk Distribution</h3>
        <ResponsiveContainer width="100%" height={250}>
          <BarChart data={Object.entries(riskSummary).map(([k, v]) => ({ name: k, value: v }))}>
            <XAxis dataKey="name" />
            <YAxis allowDecimals={false} />
            <Tooltip />
            <Bar dataKey="value" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </section>

      {/* Alert History */}
      <section className="history-card">
        <h3>📜 Alert History</h3>
        <div className="history-list">
          {history.map((item, idx) => (
            <div
              key={idx}
              className="history-item"
              style={{ borderLeft: `6px solid ${getRiskColor(item.risk_level)}` }}
            >
              <p>
                <strong>{item.time}</strong> — {item.risk_level} | HR:{" "}
                {item.heart_rate_bpm} bpm | SpO₂: {item.spo2_percent?.toFixed(1)}% | Temp:{" "}
                {item.body_temperature_c?.toFixed(1)}°C
              </p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default App;
