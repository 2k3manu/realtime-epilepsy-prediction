# Personalized Real-time Epileptic Seizure Monitoring System

## Overview (Ongoing - Capstone Project)

This project implements a robust, scalable Data Engineering pipeline dedicated to predicting the onset of epileptic seizures. By moving beyond static models, the system processes a continuous stream of **Multimodal Physiological Telemetry** (HR, SpO₂, Glucose, Stress, etc.) in real-time to generate personalized, life-saving alerts for the individual.

The system is designed to be **device-agnostic** and easily deployable, with the core logic focusing on personalized prediction thresholds rather than generic monitoring.

---

## Architecture and Technical Stack

| Component | Technology | Role in Project | Version Used |
| :--- | :--- | :--- | :--- |
| **Ingestion** | **Apache Kafka** | High-throughput backbone. Handles continuous data streaming and ensures message delivery using the **Partition Key** for user separation. | Kafka 4.1.0 (KRaft Mode) |
| **Processing (Future)** | **Apache Flink** | The dedicated stream processor. Will handle stateful processing, time windowing, and apply the personalized ML model. | (To be installed) |
| **Storage (Future)** | **Apache Cassandra** | Low-latency NoSQL store for serving real-time predictions and alerts to the React front-end. | (To be installed) |
| **Front-end/Demo** | **React.js / Python Flask** | (Future) Used to display live charts, risk scores, and the alert history log. | React.js / Flask (API) |
| **ML Training** | **Apache Spark** | (Future) Used for batch training and retraining of the specialized ML models. | PySpark |

---

## Data Source and Simulation

The project uses a Python Producer (`data_generator.py`) to simulate a continuous sensor feed.

* **Data File:** `patient_seizure_dataset.csv` (11,700 rows of multimodal data)
* **Streaming Logic:** The producer reads the CSV file and loops indefinitely, sending each row as a **JSON** message.
* **Partitioning:** The unique stream ID (`patient_A`) is used as the **Kafka Partition Key** to guarantee data ordering and integrity for Flink's personalized processing.