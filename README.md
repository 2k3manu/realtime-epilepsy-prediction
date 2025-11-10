# 🧠 Real-Time Epileptic Seizure Monitoring System

An **AI + IoT-driven Health Monitoring Platform** that continuously analyzes patient vitals to **detect and predict epileptic seizures** using **Machine Learning**, **Cassandra**, and **real-time streaming** technologies.  
The system provides an intuitive **React dashboard** for visualization and alerting.

---

## 🚀 Overview

This project focuses on building an **end-to-end pipeline** for real-time epileptic seizure detection using **AI, Data Engineering, and Full-Stack Integration**.

It combines:
- **IoT Sensor Simulation**
- **Apache Flink & Kafka** (for future live stream processing)
- **Cassandra Database** (for scalable time-series storage)
- **Python + Flask AI API** (for ML model inference)
- **Node.js Backend** (for real-time ingestion and Cassandra communication)
- **React Frontend** (for dynamic visualization)

---

## 🧠 Objectives

1. To monitor patient vital signs in real-time.  
2. To predict **risk levels** (“Normal”, “Moderate”, “High”) based on current vitals.  
3. To detect potential **epileptic seizure events** using trained ML models.  
4. To provide healthcare professionals with **instant alerts** via a dashboard.  
5. To simulate realistic health data streams for experimentation and analysis.

---

## ⚙️ System Architecture

```
IoT Data Simulation (Python)
       ↓
Kafka (Stream Queue)
       ↓
Apache Flink (Real-time Stream Processor)
       ↓
Cassandra Database (NoSQL Time-Series Storage)
       ↓
Flask API (AI Inference Engine)
       ↓
Node.js Backend (REST API Gateway)
       ↓
React Frontend (Visualization Dashboard)
```

---

## 🧩 Key Features

| Feature | Description |
|----------|--------------|
| 💓 **Real-Time Monitoring** | Continuously tracks vital data streams |
| 🧠 **AI-Driven Predictions** | Random Forest model predicts seizure risk |
| 🧾 **Cassandra Integration** | Stores structured patient time-series data |
| 🌐 **Interactive Dashboard** | React app visualizes live patient data |
| ⚙️ **Modular Architecture** | Each layer (ML, backend, UI) is decoupled |
| 🧮 **Synthetic Dataset Generator** | Automatically creates large-scale patient datasets |
| 🧰 **Scalable Infrastructure** | Flink + Kafka-ready for real deployment |

---

## 📊 Dataset Details

The dataset used (`patient_seizure_dataset.csv`) includes 13 key health parameters:

| Feature | Description |
|----------|--------------|
| `time` | Timestamp of record |
| `patient_id` | Unique patient identifier |
| `heart_rate_bpm` | Heart rate (beats per minute) |
| `spo2_percent` | Oxygen saturation |
| `body_temperature_c` | Body temperature (°C) |
| `movement_g` | Movement intensity (g-force) |
| `stress_level` | Estimated stress level (scale 1–10) |
| `blood_glucose_mgdl` | Blood glucose level (mg/dL) |
| `sleep_hours` | Hours of sleep |
| `ambient_light_lux` | Ambient light exposure |
| `noise_exposure_db` | Environmental noise level |
| `seizure_label` | Binary indicator (0 = no seizure, 1 = seizure) |
| `risk_level` | Derived class (Normal / Moderate / High) |

Dataset generated using:  
👉 `generate_synthetic_data.py`

---

## 🧠 Machine Learning Pipeline

### 🎯 Goals
Predict:
- **Seizure Label (0 or 1)**  
- **Risk Level (Normal / Moderate / High)**

### 🧮 Model Used
- **Random Forest Classifier (scikit-learn)**  
- Trained using 12,000+ synthetic records  
- Balanced with **SMOTE** and feature normalization  
- Saved models:
  - `rf_risk_model.joblib`
  - `rf_seizure_model.joblib`
  - `scaler.joblib`
  - `label_encoder.joblib`

### ⚡ Accuracy
| Model | Accuracy | Purpose |
|--------|-----------|----------|
| Risk Prediction | 1.00 | Predicts health risk |
| Seizure Detection | 1.00 | Detects seizure onset |

---

## 🧾 Installation & Setup

### 🐍 Backend + AI (Flask API)

```bash
git clone https://github.com/<your-username>/Realtime_Epileptic_Seizure_Monitoring_System.git
cd Realtime_Epileptic_Seizure_Monitoring_System
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 predictor_api.py
```

Now visit:
```
http://127.0.0.1:8000
```

---

### ⚙️ Node.js Backend (Cassandra Connector)

```bash
cd backend
npm install
node flask_app.js
```

It will connect to Cassandra and expose data through:
```
http://127.0.0.1:5000
```

---

### 🌐 Frontend (React Dashboard)

```bash
cd frontend
npm install
npm start
```

Dashboard runs on:
```
http://localhost:3000
```

Displays live vital signs, prediction results, and alert history.

---

## 🧰 Project Folder Structure

```
📦 Realtime_Epileptic_Seizure_Monitoring_System
 ┣ 📂 backend
 ┃ ┣ flask_app.js
 ┃ ┣ package.json
 ┃ ┗ package-lock.json
 ┣ 📂 frontend
 ┃ ┣ 📂 src
 ┃ ┃ ┣ components/
 ┃ ┃ ┗ App.js
 ┣ 📜 predictor_api.py
 ┣ 📜 train_rf.py
 ┣ 📜 generate_synthetic_data.py
 ┣ 📜 patient_seizure_dataset.csv
 ┣ 📜 flink_processor.py
 ┣ 📜 data_generator.py
 ┣ 📜 rf_risk_model.joblib
 ┣ 📜 rf_seizure_model.joblib
 ┣ 📜 scaler.joblib
 ┣ 📜 label_encoder.joblib
 ┣ 📜 requirements.txt
 ┗ 📜 README.md
```

---

## 🧠 How Prediction Works (Example)

**Input JSON:**
```json
{
  "heart_rate_bpm": 118,
  "spo2_percent": 96,
  "body_temperature_c": 38.3,
  "movement_g": 2.5,
  "stress_level": 7,
  "blood_glucose_mgdl": 82,
  "sleep_hours": 6.8,
  "noise_exposure_db": 45,
  "ambient_light_lux": 300
}
```

**Output JSON:**
```json
{
  "risk_level": "High",
  "seizure_label": 1,
  "status": "Prediction successful ✅"
}
```

---

## 🌍 Applications

- Real-time seizure prediction & monitoring  
- ICU alert systems  
- Smart wearable integration  
- Medical IoT data streaming  
- Preventive healthcare analytics  

---

## 🔮 Future Enhancements

- ✅ Integrate Apache Flink for real streaming  
- ✅ Enable Kafka ingestion  
- ✅ Add multi-patient visualization  
- ✅ Deploy Flask API on cloud (AWS EC2 or GCP)  
- ✅ Add mobile-responsive dashboard  

---

## 👨‍💻 Author

**Manu N M**  
Master of Computer Applications (MCA)  
PES University, Dept. of Computer Applications  
Capstone Project — 2025  

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this work with proper attribution.

---

## 🏁 Project Status

✅ AI Model — Trained & Tested  
✅ Backend — Working with Cassandra  
✅ Frontend — React Dashboard Live  
⚙️ Stream Layer — Ready for Kafka + Flink Integration

---

✨ *“Turning IoT data into life-saving insights through AI and Engineering.”* ✨
