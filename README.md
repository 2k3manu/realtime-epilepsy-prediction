# Personalized Real-time Epileptic Seizure Monitoring System

## Overview (Ongoing - Capstone Project)

This project implements a robust, scalable Data Engineering pipeline dedicated to predicting the onset of epileptic seizures. By moving beyond static models, the system processes a continuous stream of **Multimodal Physiological Telemetry** (HR, SpO₂, Glucose, Stress, etc.) in real-time to generate personalized, life-saving alerts for the individual.

The system is designed to be **device-agnostic** and easily deployable, with the core logic focusing on personalized prediction thresholds rather than generic monitoring.

---

## Architecture and Technical Stack

| Component | Technology | Role in Project | Status | Version Used |
| :--- | :--- | :--- | :--- | :--- |
| **Ingestion** | **Apache Kafka** | High-throughput backbone, keyed by individual ID for stream integrity. | **Deployed** | Kafka 4.1.0 (KRaft Mode) |
| **Processing** | **Apache Flink** | **Core Prediction Engine.** Performs stream parsing, keying, and execution of the multi-factor risk logic. | **Deployed** | Flink 2.1.0 |
| **Connector** | **KafkaSource API** | The modern, reliable method used to connect Flink to Kafka topics. | **Deployed** | Connector 4.0.1 |
| **Storage (Future)** | **Apache Cassandra** | Low-latency NoSQL store for serving alerts to the React front-end. | (To be installed) |
| **Front-end/Demo** | **React.js / Python Flask** | (Future) Used to display live charts, risk scores, and the alert history log. | (To be built) |

---

## Data Source and Streaming Configuration

* **Data File:** `patient_seizure_dataset.csv` (11,700 rows of multimodal data)
* **Streaming Logic:** The `data_generator.py` streams data using the **correct API version** for Kafka 4.1.0 and utilizes the `UNIQUE_STREAM_ID` as the Partition Key.
* **Key Achievement:** Successfully resolved all complex WSL/Java classpath and resource allocation issues to achieve **full end-to-end streaming output** in the Flink Task Manager logs.