# 🧠 Personalized Real-time Epileptic Seizure Monitoring System  

## 📘 Overview  

This project implements a **complete end-to-end data engineering and AI-driven analytics pipeline** for *real-time epileptic seizure prediction and monitoring*.  
It integrates **Kafka**, **Flink**, **Cassandra**, and **Machine Learning** with an interactive **React.js dashboard** to predict and visualize seizure risks in real-time.

The system continuously processes multimodal biosignals such as:  
**Heart Rate, SpO₂, Temperature, Movement, Stress, Glucose, Sleep, Noise, and Light Exposure** — to generate personalized alerts predicting seizure onset.  

---

## 🏗️ System Architecture  

| Layer | Technology | Purpose | Status |
| :---- | :---------- | :-------- | :------ |
| **Data Ingestion** | **Apache Kafka (v4.1.0, KRaft)** | Real-time data stream backbone, keyed by patient ID | ✅ Completed |
| **Stream Processing** | **Apache Flink (v2.1.0)** | Stateful event processing, multimodal risk analysis | ✅ Completed |
| **Data Storage** | **Apache Cassandra (v4.1.10)** | Scalable time-series database for telemetry and alerts | ✅ Completed |
| **AI Model Training** | **Random Forest (scikit-learn)** | Predicts `seizure_label` and `risk_level` based on vitals | ✅ Completed |
| **Backend API** | **Flask / Node.js (Express)** | Exposes endpoints for data retrieval and AI inference | ✅ Integrated |
| **Frontend Visualization** | **React.js (CRA)** | Interactive dashboard for live patient monitoring | ✅ Deployed |

---

## ⚙️ Data & Model Pipeline  

### 🧾 Dataset  
**File:** `patient_seizure_dataset.csv`  
**Rows:** 12,000 synthetic multimodal patient readings  

**Features:**
- `patient_id`, `timestamp`
- `heart_rate_bpm`, `spo2_percent`, `body_temperature_c`
- `movement_g`, `stress_level`, `sleep_hours`
- `noise_exposure_db`, `ambient_light_lux`
- `blood_glucose_mgdl`, `seizure_label`, `risk_level`

The dataset was generated using statistical simulation via `generate_synthetic_data.py`, ensuring realistic physiological trends under both seizure and normal conditions.

---

### 🧠 Model Training  
**Script:** `train_rf.py`  
**Algorithm:** Random Forest Classifier  
**Targets:**  
- `risk_level` → {0: Normal, 1: Moderate, 2: High}  
- `seizure_label` → {0: No Seizure, 1: Seizure}  

**Generated Model Files:**
- `rf_risk_model.joblib`
- `rf_seizure_model.joblib`
- `label_encoder.joblib`
- `scaler.joblib`

**Performance Metrics (Synthetic Data):**
| Metric | Risk Level | Seizure Label |
| :------ | :----------: | :-------------: |
| Accuracy | 100% | 100% |
| F1-Score | 1.00 | 1.00 |
| Precision | 1.00 | 1.00 |
| Recall | 1.00 | 1.00 |

---

## 🧩 Backend API (Flask / Node.js)

The backend interacts with **Cassandra** to serve endpoints for:
- Inserting live sensor data  
- Fetching latest vitals  
- Predicting `risk_level` and `seizure_label`  

It acts as a bridge between the streaming data pipeline and the visualization dashboard.

---

## 💻 Frontend (React.js)

**Folder:** `frontend/`  
Developed using **React (Create React App)**  

### Key Features:
- Real-time patient vitals display  
- Color-coded risk level indicators  
- Live alert history feed  
- Responsive modern UI with live updates  

### Components:
- `VitalsCard.js` → Real-time vital display  
- `VitalsChart.js` → Visual trends of patient vitals  
- `AlertCard.js` → Alerts and risk-level changes  
- `Navbar.js` → Application navigation  

---

## 🧠 Real-time Stream Workflow  

```bash
Data Generator (Python)
        ↓
Kafka Producer (epilepsy_telemetry topic)
        ↓
Flink Processor (stateful transformation + risk inference)
        ↓
Cassandra (persistent storage)
        ↓
Flask / Node.js API (data access layer)
        ↓
React.js Frontend (live dashboard)

```

---

## 🧾 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/2k3manu/realtime-epilepsy-monitor.git
cd realtime-epilepsy-monitor

2️⃣ Backend Setup
cd backend
npm install
npm start

3️⃣ Frontend Setup
cd frontend
npm install
npm start

4️⃣ Python Virtual Environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

5️⃣ Train or Re-train the AI Model
python3 train_rf.py

---

## 🧰 Project Folder Structure

```bash
Realtime_Epileptic_Seizure_Monitoring_System/
│
├── backend/
│   ├── flask_app.js
│   ├── package.json
│   └── package-lock.json
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── package-lock.json
│
├── data_generator.py
├── flink_processor.py
├── generate_synthetic_data.py
├── patient_seizure_dataset.csv
├── train_rf.py
├── rf_risk_model.joblib
├── rf_seizure_model.joblib
├── label_encoder.joblib
├── scaler.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🌍 Applications

- Wearable IoT Health Devices
- Remote Patient Health Monitoring
- ICU Vital Analytics
- Predictive Clinical Decision Support Systems

---

## 👨‍💻 Author

**Manu N M**  
🎓 MCA, PES University  
📫 [GitHub: 2k3manu](https://github.com/2k3manu/realtime-epilepsy-monitor)

---

## 🧾 License
This project is part of the **PES University MCA Capstone (UQ24CA741A)** program.  
For academic and non-commercial research purposes only.
