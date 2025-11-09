// ===============================
// flask_app.js (Node.js Backend)
// ===============================
import express from "express";
import cors from "cors";
import cassandra from "cassandra-driver";

const app = express();
app.use(cors());
app.use(express.json());

// Cassandra connection
const client = new cassandra.Client({
  contactPoints: ["127.0.0.1"],
  localDataCenter: "datacenter1",
  keyspace: "epilepsy_monitoring",
});

// Connect to Cassandra
client.connect()
  .then(() => console.log("✅ Connected to Cassandra (epilepsy_monitoring)"))
  .catch((err) => console.error("❌ Cassandra Connection Error:", err));

// --------------------
// Utility Functions
// --------------------

// Sleep hours constant for one session/day
let constantSleepHours = (Math.random() * 3 + 6).toFixed(1); // 6–9 hours constant
let lastSleepReset = new Date();

function resetDailySleepIfNeeded() {
  const now = new Date();
  if (now - lastSleepReset >= 24 * 60 * 60 * 1000) {
    constantSleepHours = (Math.random() * 3 + 6).toFixed(1);
    lastSleepReset = now;
    console.log(`🌙 Sleep hours reset for new day: ${constantSleepHours} hrs`);
  }
}

// Generate simulated vitals
function generateSimulatedData() {
  resetDailySleepIfNeeded();

  const hr = Math.floor(Math.random() * (140 - 55) + 55);
  const spo2 = (Math.random() * (100 - 85) + 85).toFixed(2);
  const temp = (Math.random() * (39 - 36) + 36).toFixed(2);
  const move = (Math.random() * 4).toFixed(2);
  const stress = Math.floor(Math.random() * 10) + 1;
  const glucose = Math.floor(Math.random() * (160 - 65) + 65);
  const sleep = parseFloat(constantSleepHours);
  const noise = (Math.random() * (70 - 20) + 20).toFixed(2);
  const light = (Math.random() * (500 - 100) + 100).toFixed(2);
  const seizure = Math.random() < 0.2 ? 1 : 0;

  // Risk logic
  let risk = "Normal";
  if (hr > 120 || spo2 < 90 || temp > 38.0 || stress > 8 || glucose < 70) {
    risk = "High";
  } else if (hr > 100 || stress > 6 || temp > 37.5) {
    risk = "Moderate";
  }

  return {
    patient_id: "patient_1",
    heart_rate_bpm: hr,
    spo2_percent: parseFloat(spo2),
    body_temperature_c: parseFloat(temp),
    movement_g: parseFloat(move),
    stress_level: stress,
    blood_glucose_mgdl: glucose,
    sleep_hours: sleep,
    noise_exposure_db: parseFloat(noise),
    ambient_light_lux: parseFloat(light),
    seizure_label: seizure,
    risk_level: risk,
  };
}

// --------------------
// API ROUTES
// --------------------

app.get("/api/vitals", async (req, res) => {
  try {
    const data = generateSimulatedData();

    const query = `
      INSERT INTO vitals_data (
        patient_id, timestamp, heart_rate_bpm, spo2_percent,
        body_temperature_c, movement_g, stress_level,
        blood_glucose_mgdl, sleep_hours, noise_exposure_db,
        ambient_light_lux, seizure_label, risk_level
      ) VALUES (?, toTimestamp(now()), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    `;

    await client.execute(
      query,
      [
        data.patient_id,
        data.heart_rate_bpm,
        data.spo2_percent,
        data.body_temperature_c,
        data.movement_g,
        data.stress_level,
        data.blood_glucose_mgdl,
        data.sleep_hours,
        data.noise_exposure_db,
        data.ambient_light_lux,
        data.seizure_label,
        data.risk_level,
      ],
      { prepare: true }
    );

    console.table(data);
    res.json(data);
  } catch (err) {
    console.error("❌ Error inserting or fetching vitals:", err);
    res.status(500).json({ message: "Internal Server Error" });
  }
});

// --------------------
// Start the Server
// --------------------
const PORT = 5000;
app.listen(PORT, "0.0.0.0", () =>
  console.log(`🚀 Node.js API Server running at http://127.0.0.1:${PORT}`)
);
