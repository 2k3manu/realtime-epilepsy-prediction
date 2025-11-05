import { useState, useEffect } from "react";
import Navbar from "./components/Navbar";
import VitalsCard from "./components/VitalsCard";
import AlertCard from "./components/AlertCard";
import VitalsChart from "./components/VitalsChart";

function App() {
  // --- Vital States ---
  const [heartRate, setHeartRate] = useState(82);
  const [temperature, setTemperature] = useState(36.7);
  const [movement, setMovement] = useState(1.2);

  // --- Alert States ---
  const [alert, setAlert] = useState({
    message: "✅ All vitals stable",
    level: "normal",
  });
  const [alertHistory, setAlertHistory] = useState([]);
  const [chartData, setChartData] = useState([]);

  // --- Generate Live Simulated Data ---
  useEffect(() => {
    const interval = setInterval(() => {
      // Heart Rate: baseline with small variation
      setHeartRate((prev) => {
        let change = (Math.random() - 0.5) * 10;
        return Math.max(55, Math.min(150, prev + change));
      });

      // Temperature: slow and mild fluctuation
      setTemperature((prev) => {
        let change = (Math.random() - 0.5) * 0.3;
        return Math.max(35.2, Math.min(38.0, prev + change));
      });

      // Movement: realistic — fluctuates near baseline, occasional spikes
      setMovement((prev) => {
        if (Math.random() < 0.1) return Math.random() * 3.5 + 0.5; // simulate jerks
        let baseline = 1.5 + (Math.random() - 0.5) * 0.8;
        return Math.max(0, Math.min(4, baseline));
      });
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  // --- Update Sliding Chart ---
  useEffect(() => {
    const newPoint = {
      time: new Date().toLocaleTimeString().split(" ")[0],
      heartRate,
      temperature,
      movement,
    };
    setChartData((prev) => {
      const updated = [...prev, newPoint];
      return updated.length > 60 ? updated.slice(updated.length - 60) : updated;
    });
  }, [heartRate, temperature, movement]);

  // --- Intelligent Alert System ---
  useEffect(() => {
    let newLevel = "normal";
    let msg = "✅ All vitals stable";

    if (heartRate > 110 || temperature > 37.6 || movement > 3.0) {
      newLevel = "high";
      msg = `🚨 High Risk Detected | HR: ${heartRate.toFixed(
        0
      )} bpm, Temp: ${temperature.toFixed(1)}°C, Move: ${movement.toFixed(2)}g`;
    } else if (heartRate > 90 || temperature > 37.2 || movement > 1.8) {
      newLevel = "medium";
      msg = `⚠️ Moderate Risk | HR: ${heartRate.toFixed(
        0
      )} bpm, Temp: ${temperature.toFixed(1)}°C, Move: ${movement.toFixed(2)}g`;
    }

    // Only record new alert when level changes
    setAlert((prev) => {
      if (prev.level !== newLevel) {
        setAlertHistory((prevHistory) => [
          { message: msg, time: new Date().toLocaleTimeString() },
          ...prevHistory,
        ]);
      }
      return { message: msg, level: newLevel };
    });
  }, [heartRate, temperature, movement]);

  // --- JSX UI ---
  return (
    <div>
      <Navbar />

      {/* Title */}
      <div style={{ textAlign: "center", marginTop: "30px" }}>
        <h2>🧠 Personalized Real-time Epileptic Seizure Monitor</h2>
        <p style={{ color: "#666" }}>
          Simulating live patient vitals and seizure risk detection
        </p>
      </div>

      {/* Vital Cards */}
      <div style={{ display: "flex", justifyContent: "center", flexWrap: "wrap" }}>
        <VitalsCard
          title="Heart Rate"
          value={heartRate.toFixed(0)}
          unit="bpm"
          color="#E63946"
        />
        <VitalsCard
          title="Body Temp"
          value={temperature.toFixed(1)}
          unit="°C"
          color="#457B9D"
        />
        <VitalsCard
          title="Movement"
          value={movement.toFixed(2)}
          unit="g"
          color="#2A9D8F"
        />
      </div>

      {/* Alert Display */}
      <div style={{ marginTop: "30px" }}>
        <AlertCard message={alert.message} level={alert.level} />
      </div>

      {/* Live Chart */}
      <VitalsChart data={chartData} />

      {/* Alert History */}
      <div
        style={{
          width: "60%",
          margin: "30px auto",
          textAlign: "left",
          background: "#f5f5f5",
          padding: "15px",
          borderRadius: "10px",
          boxShadow: "0 2px 6px rgba(0,0,0,0.1)",
        }}
      >
        <h3>🕒 Alert History</h3>
        {alertHistory.length === 0 ? (
          <p>No alerts generated yet.</p>
        ) : (
          <ul>
            {alertHistory.map((entry, index) => (
              <li key={index}>
                <strong>{entry.time}</strong>: {entry.message}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;
