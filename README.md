# Personalized Real-time Epileptic Seizure Monitoring System

## Overview (Ongoing - Capstone Project)

This project implements a robust, scalable **Data Engineering pipeline** dedicated to predicting the onset of epileptic seizures. By moving beyond static models, the system processes a continuous stream of **Multimodal Physiological Telemetry** (HR, SpO₂, Glucose, Stress, etc.) in real-time to generate **personalized, life-saving alerts** for the individual.

The system is designed to be **device-agnostic** and easily deployable, with the core logic focusing on personalized prediction thresholds rather than generic monitoring.

---

## Architecture and Technical Stack

| Component | Technology | Role in Project | Status | Version Used |
| :--- | :--- | :--- | :--- | :--- |
| **Ingestion** | **Apache Kafka** | High-throughput backbone, keyed by individual ID for stream integrity. | **Deployed** | Kafka 4.1.0 (KRaft Mode) |
| **Processing** | **Apache Flink** | **Core Prediction Engine.** Executes Keying, Stateful Processing, and Multimodal Risk Calculation. | **Deployed** | Flink 2.1.0 |
| **Serving Layer** | **Apache Cassandra** | **Final Database Sink.** Low-latency NoSQL store for serving real-time alerts to the front-end. | **Deployed** | Cassandra 4.1.10 |
| **Connector** | **KafkaSource API** | The modern, reliable method used to connect Flink to Kafka topics. | **Deployed** | Connector 4.0.1 |
| **Front-end/Demo** | **React.js / Python Flask** | User dashboard for displaying live charts, risk scores, and the alert history log. | (To be Built) |

---

## Data Source and Streaming Configuration

* **Data File:** `patient_seizure_dataset.csv` (11,700 rows of multimodal data)
* **Streaming Logic:** The `data_generator.py` streams data using the correct API version for Kafka 4.1.0 and utilizes the `UNIQUE_STREAM_ID` as the Partition Key.
* **Key Achievement:** Successfully built the **full end-to-end backend pipeline** (Producer -> Kafka -> Flink -> Cassandra) and resolved all major integration and resource allocation issues.

---

## Progress Tracker & Next Steps 💾

| Milestone | Key Component | Status |
| :--- | :--- | :--- |
| **PHASE 1: Ingestion** | Kafka Setup, Python Producer, Data Streaming | Complete |
| **PHASE 2: Processing** | Flink Cluster, `flink_processor.py`, Multimodal Prediction Logic | Complete |
| **PHASE 3: Serving Layer**| **Cassandra 4.1.10 Setup**, Flink Cassandra Sink Integration | Complete |
| **PHASE 4: Front-end/API** | **Python Flask API** to read Cassandra and **React Dashboard** (Visualization). | **Starting Next Session** |

***