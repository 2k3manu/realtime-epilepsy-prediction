# 🧠 Personalized Real-time Epileptic Seizure Monitoring System  

## 📘 Overview

This project is a **complete end-to-end real-time monitoring pipeline** built as part of the MCA Capstone Project (PES University).  
It predicts and visualizes seizure risks by analyzing **multimodal physiological signals** such as Heart Rate, Body Temperature, and Movement.  

The system is:
- **Device-agnostic** – can integrate with any medical wearable or IoT sensor  
- **Real-time** – powered by Kafka, Flink, and Cassandra backend pipeline  
- **Interactive** – now includes a live **React dashboard frontend**

---

## 🏗️ System Architecture

| Layer | Technology | Description | Status |
|-------|-------------|-------------|---------|
| **Ingestion Layer** | 🧩 Apache Kafka 4.1.0 | Streams real-time vitals data keyed by patient ID | ✅ Completed |
| **Processing Layer** | ⚙️ Apache Flink 2.1.0 | Performs multimodal risk analysis with stateful stream processing | ✅ Completed |
| **Serving Layer** | 🗄️ Apache Cassandra 4.1.10 | Low-latency NoSQL store for telemetry and alert history | ✅ Completed |
| **Frontend Layer** | 🌐 React.js (Create React App) | Displays real-time vitals, risk alerts, and alert history graphically | ✅ Completed |
| **API Layer** | 🧠 Flask (Upcoming) | REST API bridge between Cassandra and Frontend for live data | 🔜 In Progress |

---

## ⚙️ Frontend Functionality (React Dashboard)

**Live Simulation Features:**
- Real-time updates every 2 seconds for Heart Rate, Temperature, and Movement  
- Intelligent **risk classification** (Normal / Moderate / High)  
- **Auto recovery detection** when vitals stabilize  
- 60-point **sliding window chart** showing continuous fluctuations  
- **Alert history log** storing transitions between risk levels  

**Key React Components:**
- `VitalsCard.js` – Shows live readings  
- `AlertCard.js` – Displays current status with color codes  
- `VitalsChart.js` – Line graph visualization  
- `Navbar.js` – Simple app navigation bar  
- `App.js` – Main logic combining live simulation and state tracking  

---

## 🧠 Simulation Logic (Frontend)

| Vital | Range | Behavior |
|--------|--------|-----------|
| **Heart Rate (bpm)** | 55 – 150 | Random baseline drift with natural variability |
| **Temperature (°C)** | 35.2 – 38.0 | Mild slow fluctuations |
| **Movement (g)** | 0 – 4 | Small random motion with occasional sudden spikes (seizure simulation) |

---

## 🧩 Phase-wise Progress Tracker

| Phase | Component | Deliverables | Status |
|-------|------------|---------------|---------|
| **Phase 1** | Kafka Ingestion | Python producer & streaming to topic | ✅ Completed |
| **Phase 2** | Flink Processing | Multimodal real-time risk detection | ✅ Completed |
| **Phase 3** | Cassandra Serving | Data persistence for telemetry & alerts | ✅ Completed |
| **Phase 4** | React Frontend | Real-time visualization dashboard | ✅ Completed |
| **Phase 5** | Flask API + Deployment | REST integration, hosting on cloud | 🔜 Next Phase |

---

## 🌍 Real-world Application

- Predictive healthcare systems  
- Wearable IoT medical devices  
- ICU and remote patient monitoring  
- Early seizure alerting systems  

---

## 👨‍💻 Author

**Manu N M**  
🎓 MCA, PES University  
📫 [GitHub: 2k3manu](https://github.com/2k3manu/realtime-epilepsy-monitor)

---

## 🧾 License
This project is part of **PES University MCA Capstone (UQ24CA741A)**.  
For academic and non-commercial research purposes only.

---