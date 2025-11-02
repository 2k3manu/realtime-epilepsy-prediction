import json
import time
import pandas as pd
import numpy as np
from kafka import KafkaProducer
from datetime import datetime

# --- CONFIGURATION ---
# Using 127.0.0.1 for reliable connection from WSL to Windows Kafka broker
KAFKA_SERVER = '127.0.0.1:9092' 
KAFKA_TOPIC = 'epilepsy_telemetry'

# Unique ID used as the Kafka Partition Key for stream separation
UNIQUE_STREAM_ID = 'patient_A' 
DATA_FILE = 'patient_seizure_dataset.csv' 
# ---------------------------------

def generate_telemetry_stream():
    """
    Simulates a live, continuous telemetry stream by reading and looping 
    through the comprehensive dataset. This acts as the Kafka Producer.
    """
    producer = None 
    try:
        # 1. Load the comprehensive dataset
        df = pd.read_csv(DATA_FILE)
        
        # Ensure the timestamp column is in a useful format
        df['time'] = pd.to_datetime(df['time'])

        print(f"Loaded {len(df)} historical records for simulation.")
        
        # 2. Initialize Kafka Producer
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            
            # CRITICAL FIX: Force the client to use a modern API version range.
            # (0, 11, 5) corresponds to Kafka 0.11.0.0, which is the baseline 
            # for modern protocols and allows negotiation up to 4.1.0.
            api_version=(0, 11, 5), 
            request_timeout_ms=30000 
        )
        print(f"Kafka Producer connected. Target Topic: {KAFKA_TOPIC}")
        print(f"Streaming data for individual: {UNIQUE_STREAM_ID}")

        # 3. Start Continuous Streaming Loop
        row_index = 0
        while True:
            # Loop back to the start of the data when finished
            if row_index >= len(df):
                print("--- Looping Data: Restarting Stream ---")
                row_index = 0

            # Get current row and convert to a dictionary
            row_data = df.iloc[row_index].to_dict()
            
            # Ensure data types are handled (convert Timestamp/numpy types to string/native type)
            record = {
                k: (v if not isinstance(v, (pd.Timestamp, np.generic)) else str(v)) 
                for k, v in row_data.items()
            }
            
            # Add the necessary key for partitioning
            record['unique_stream_id'] = UNIQUE_STREAM_ID 
            
            # Log the data being sent (showing key features)
            print(f"[{row_index:05d}] Sending | HR: {record['heart_rate_bpm']} | SpO2: {record['spo2_percent']} | Glucose: {record['blood_glucose_mgdl']} | Label: {record['seizure_label']}")

            # 4. Produce the message to Kafka
            # The 'key' ensures Flink receives data consistently for this individual
            producer.send(
                KAFKA_TOPIC, 
                key=UNIQUE_STREAM_ID.encode('utf-8'),
                value=record
            )
            
            row_index += 1
            # Simulate a 1-second delay for a real-time sensor reading
            time.sleep(1) 

    except FileNotFoundError:
        print(f"\nERROR: Data file '{DATA_FILE}' not found. Please ensure the CSV is in the same directory.")
    except Exception as e:
        print(f"\nAn error occurred during Kafka production: {e}")
    finally:
        # Close producer cleanly only if it was successfully initialized
        if producer:
            producer.close()

if __name__ == "__main__":
    generate_telemetry_stream()