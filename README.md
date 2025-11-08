# 🧠 Personalized Real-time Epileptic Seizure Monitoring System  

## 📘 Overview
This MCA Capstone Project implements a **real-time, scalable health analytics pipeline** for predicting and monitoring epileptic seizures.  
It continuously streams multimodal biosignals — **Heart Rate, SpO₂, Temperature, Movement, Stress, Glucose, Medication Intake, and Environmental Factors** — to predict potential seizure risk in real time.

The system is **device-agnostic**, meaning it can ingest telemetry from *any wearable or medical IoT device* via Kafka.

---

## 🏗️ System Architecture & Technology Stack

| Layer | Technology | Description | Status |
| :---- | :---------- | :----------- | :------ |
| **Data Ingestion** | 🧩 Apache Kafka 4.1.0 (KRaft Mode) | High-throughput data streaming backbone. | ✅ Completed |
| **Stream Processing** | ⚙️ Apache Flink 2.1.0 | Performs stateful multimodal risk calculation. | ✅ Completed |
| **Storage/Serving Layer** | 🗄️ Apache Cassandra 4.1.10 | Stores telemetry and alert data for real-time visualization. | ✅ Completed |
| **Backend API** | 🧠 Node.js + Express | Exposes REST API for React to fetch live vitals from Cassandra. | ✅ Completed |
| **Frontend Dashboard** | 🌐 React.js | Displays real-time graphs, risk alerts, and vitals. | 🚧 In Progress |

---

## ⚙️ Data & Backend Configuration

- **Dataset:** `patient_seizure_dataset.csv` (~11,700 rows, multimodal telemetry).
- **Cassandra Table:** `vitals_data`  
  Includes attributes like:
  - `heart_rate_bpm`, `spo2_percent`, `body_temperature_c`, `movement_g`, `stress_level`,  
    `blood_glucose_mgdl`, `medication_taken`, `sleep_hours`, `noise_exposure_db`,  
    `ambient_light_lux`, `seizure_label`, and computed `risk_level`.
- **Backend Server:**  
  - File: `backend/flask_app.js`  
  - Port: `5000`  
  - Endpoint: `/api/vitals`

✅ Successfully connected **Node.js → Cassandra → React** for real-time analytics.

---

## 🧩 Phase-wise Progress Tracker

| Phase | Component | Deliverables | Status |
| :---- | :---------- | :------------ | :------ |
| **Phase 1** | Kafka Ingestion | Topic setup, Python Producer, stream verification | ✅ Completed |
| **Phase 2** | Flink Processing | Stateful prediction logic, feature extraction | ✅ Completed |
| **Phase 3** | Cassandra Storage | Schema design, risk-level aggregation | ✅ Completed |
| **Phase 4** | Node.js API | Express server for Cassandra data fetch | ✅ Completed |
| **Phase 5** | React Frontend | Live visualization dashboard | 🚧 Ongoing |

---

## 🌍 Applications

- Remote patient monitoring systems  
- Smart healthcare IoT devices  
- Predictive seizure detection for epilepsy patients  
- Hospital telemetry and data-driven alerts  

---

## 👨‍💻 Author

**Manu N M**  
🎓 MCA, PES University  
📫 [GitHub: 2k3manu](https://github.com/2k3manu/realtime-epilepsy-monitor)

---

## 🧾 License
This project is part of the **PES University MCA Capstone (UQ24CA741A)** program.  
For academic and non-commercial research purposes only.
