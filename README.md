# 🧠 Personalized Real-time Epileptic Seizure Monitoring System  

## 📘 Overview

This capstone project implements a **scalable data engineering pipeline** for *real-time prediction and monitoring of epileptic seizures*.  
The system ingests multimodal biosignal data — **Heart Rate, SpO₂, Glucose, Stress, Movement, Medication Intake**, etc. — and performs **continuous, personalized analysis** to anticipate seizures before onset.

Unlike typical research models that depend on static EEG datasets or device-specific APIs, this system is **device-agnostic** and can integrate telemetry from *any medical wearable or IoT source* through its Kafka ingestion layer.

---

## 🏗️ System Architecture & Technology Stack

| Layer | Technology | Description | Status |
| :---- | :---------- | :----------- | :------ |
| **Ingestion Layer** | 🧩 **Apache Kafka 4.1.0 (KRaft Mode)** | High-throughput, real-time data streaming backbone keyed by patient ID. | ✅ Completed |
| **Processing Layer** | ⚙️ **Apache Flink 2.1.0** | Stateful stream processing engine performing dynamic threshold analysis and multimodal risk fusion. | ✅ Completed |
| **Storage/Serving Layer** | 🗄️ **Apache Cassandra 4.1.10** | Distributed NoSQL database optimized for low-latency writes and scalable storage of alerts and telemetry. | ✅ Completed |
| **Integration Connector** | 🔗 **KafkaSource API 4.0.1** | Modern Flink-Kafka bridge for consuming messages efficiently and reliably. | ✅ Completed |
| **Frontend & API Layer** | 🌐 **Python Flask + React.js (Planned)** | Web dashboard to visualize live biosignal charts, seizure alerts, and historical logs. | 🏗️ In Progress |

---

## ⚙️ Data & Streaming Configuration

- **Dataset:** `patient_seizure_dataset.csv` containing 11,700 rows of multimodal features.  
- **Producer:** `data_generator.py` streams each record into Kafka topic `epilepsy_telemetry` with a unique key per patient.  
- **Processor:** `flink_processor.py` reads the stream, computes multimodal risk factors, and writes alerts into Cassandra.  
- **Sink:** Cassandra tables store both telemetry and alert history for the visualization layer.

✅ **End-to-End Pipeline Built & Verified:**  
Producer ➜ Kafka ➜ Flink ➜ Cassandra  

---

## 🧩 Phase-wise Progress Tracker

| Phase | Component | Deliverables | Status |
| :---- | :---------- | :------------ | :------ |
| **Phase 1** | Kafka Ingestion | Topic setup, producer integration, stream verification | ✅ Completed |
| **Phase 2** | Flink Processing | Stateful processing, real-time risk analysis | ✅ Completed |
| **Phase 3** | Cassandra Serving | Sink integration, schema design, query validation | ✅ Completed |
| **Phase 4** | Frontend/API Layer | Flask REST API + React-based dashboard | 🚧 Ongoing |
| **Phase 5** | Final Demo & Optimization | Real-time visualization, performance tuning | 🔜 Upcoming |

---

## 🌍 Real-world Application

This framework can be extended to:
- **Remote patient monitoring systems**
- **ICU telemetry analysis**
- **Wearable IoT health devices**
- **Predictive healthcare analytics**

The system ensures **scalability, fault tolerance, and low-latency alerting**, making it deployable in both **hospital environments and consumer health ecosystems**.

---

## 👨‍💻 Author

**Manu N M**  
🎓 MCA, PES University  
📫 [GitHub: 2k3manu](https://github.com/2k3manu/realtime-epilepsy-monitor)

---

## 🧾 License
This project is part of the **PES University MCA Capstone (UQ24CA741A)** program.  
For academic and non-commercial research purposes only.

---