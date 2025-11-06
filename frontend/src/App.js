import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [vitals, setVitals] = useState(null);
  const [error, setError] = useState(null);

  // Function to fetch data from Flask API
  const fetchVitals = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/vitals");
      if (!response.ok) throw new Error("Network response was not ok");
      const data = await response.json();
      setVitals(data);
      setError(null);
    } catch (error) {
      console.error("Error fetching vitals:", error);
      setError("Unable to fetch data. Flask API might be offline.");
    }
  };

  // Refresh every 3 seconds
  useEffect(() => {
    fetchVitals();
    const interval = setInterval(fetchVitals, 3000);
    return () => clearInterval(interval);
  }, []);

  // Dynamic color based on risk level
  const getRiskColor = (level) => {
    if (level === "High") return "high-risk";
    if (level === "Moderate") return "moderate-risk";
    return "normal-risk";
  };

  return (
    <div className="dashboard">
      <h1>🧠 Real-time Epileptic Seizure Monitoring</h1>

      {error && <p className="error">{error}</p>}

      {!vitals ? (
        <p className="loading">Loading live data...</p>
      ) : (
        <>
          <div className={`risk-banner ${getRiskColor(vitals.risk_level)}`}>
            <h2>Current Risk Level: {vitals.risk_level}</h2>
          </div>

          <div className="vitals-grid">
            <div className="vital-card">
              <h3>❤️ Heart Rate</h3>
              <p>{vitals.heart_rate_bpm} bpm</p>
            </div>
            <div className="vital-card">
              <h3>🩸 SpO₂</h3>
              <p>{vitals.spo2_percent}%</p>
            </div>
            <div className="vital-card">
              <h3>🌡️ Temperature</h3>
              <p>{vitals.body_temperature_c.toFixed(1)} °C</p>
            </div>
            <div className="vital-card">
              <h3>🏃 Movement</h3>
              <p>{vitals.movement_g.toFixed(2)} g</p>
            </div>
            <div className="vital-card">
              <h3>😰 Stress Level</h3>
              <p>{vitals.stress_level}</p>
            </div>
            <div className="vital-card">
              <h3>🍬 Glucose</h3>
              <p>{vitals.blood_glucose_mgdl} mg/dL</p>
            </div>
            <div className="vital-card">
              <h3>💊 Medication Taken</h3>
              <p>{vitals.medication_taken ? "Yes" : "No"}</p>
            </div>
            <div className="vital-card">
              <h3>💤 Sleep Hours</h3>
              <p>{vitals.sleep_hours} hrs</p>
            </div>
            <div className="vital-card">
              <h3>🔊 Noise Exposure</h3>
              <p>{vitals.noise_exposure_db} dB</p>
            </div>
            <div className="vital-card">
              <h3>💡 Ambient Light</h3>
              <p>{vitals.ambient_light_lux} lux</p>
            </div>
            <div className="vital-card">
              <h3>⚡ Seizure Label</h3>
              <p>{vitals.seizure_label === 1 ? "Detected" : "None"}</p>
            </div>
          </div>

          <p className="timestamp">
            🕒 Last Updated: {new Date(vitals.timestamp).toLocaleString()}
          </p>
        </>
      )}
    </div>
  );
}

export default App;
