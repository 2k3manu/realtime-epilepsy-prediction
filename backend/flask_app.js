// ================================
// 🧠 Epileptic Seizure Monitoring - Node.js Backend
// ================================

// Import required modules
import express from "express";
import cors from "cors";
import cassandra from "cassandra-driver";

// Initialize Express app
const app = express();
app.use(cors());
app.use(express.json());

// Cassandra connection configuration
const client = new cassandra.Client({
  contactPoints: ["127.0.0.1"], // Cassandra running on local WSL
  localDataCenter: "datacenter1",
  keyspace: "epilepsy_monitoring",
});

// Connect to Cassandra
client.connect()
  .then(() => {
    console.log("✅ Connected to Cassandra (keyspace: epilepsy_monitoring)");
  })
  .catch((err) => {
    console.error("❌ Cassandra connection failed:", err);
  });

// API Route — Fetch latest record from Cassandra
app.get("/api/vitals", async (req, res) => {
  try {
    const query = `
      SELECT patient_id, timestamp, heart_rate_bpm, spo2_percent, body_temperature_c,
             movement_g, stress_level, blood_glucose_mgdl, medication_taken, sleep_hours,
             noise_exposure_db, ambient_light_lux, seizure_label, risk_level
      FROM vitals_data
      WHERE patient_id = 'patient_1'
      LIMIT 1;
    `;

    const result = await client.execute(query);

    if (result.rows.length === 0) {
      return res.status(404).json({ message: "No data found in vitals_data table." });
    }

    const data = result.rows[0];
    res.json({
      patient_id: data.patient_id,
      heart_rate_bpm: data.heart_rate_bpm,
      spo2_percent: data.spo2_percent,
      body_temperature_c: data.body_temperature_c,
      movement_g: data.movement_g,
      stress_level: data.stress_level,
      blood_glucose_mgdl: data.blood_glucose_mgdl,
      medication_taken: data.medication_taken,
      sleep_hours: data.sleep_hours,
      noise_exposure_db: data.noise_exposure_db,
      ambient_light_lux: data.ambient_light_lux,
      seizure_label: data.seizure_label,
      risk_level: data.risk_level,
      timestamp: data.timestamp,
    });
  } catch (error) {
    console.error("Error fetching data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

// Root route
app.get("/", (req, res) => {
  res.json({ message: "Epileptic Seizure Monitoring API Running" });
});

// Start the server
const PORT = 5000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`🚀 Node.js API Server running at http://0.0.0.0:${PORT}`);
});
