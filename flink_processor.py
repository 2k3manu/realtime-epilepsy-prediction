import os
import json
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import WatermarkStrategy
from pyflink.datastream.connectors.kafka import KafkaSource
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
from pyflink.datastream.functions import MapFunction

# CRITICAL: Import the Cassandra Sink and time utility
from pyflink.datastream.connectors.cassandra import CassandraSink
import time 
from datetime import datetime

# --- CONFIGURATION ---
KAFKA_SERVER = '127.0.0.1:9092'
KAFKA_SOURCE_TOPIC = 'epilepsy_telemetry'
CASSANDRA_HOST = '127.0.0.1' 
# ----------------------

def parse_json(json_string):
    """
    Converts the raw JSON string (value) from Kafka into a structured tuple (8 fields).
    """
    try:
        data = json.loads(json_string)
        return (
            # 0: Unique ID (Partition Key)
            data.get('unique_stream_id'),
            # 1: Timestamp (for Event Time processing later)
            data.get('time'), 
            # 2: HR (Int)
            data.get('heart_rate_bpm', 0),
            # 3: SpO2 (Float)
            data.get('spo2_percent', 0.0),
            # 4: Movement (Float)
            data.get('movement_g', 0.0),
            # 5: Stress (Int)
            data.get('stress_level', 0),
            # 6: Medication (Int - 1/0)
            data.get('medication_taken', 1),
            # 7: Glucose (Int)
            data.get('blood_glucose_mgdl', 90)
        )
    except Exception as e:
        return ("unknown", str(datetime.now()), 0, 0.0, 0.0, 0, 0, 0)

class CassandraMapper(MapFunction):
    """Maps the alert string into the exact tuple format required for the Cassandra INSERT statement."""
    def map(self, alert_string):
        # Input: [⚠ ALERT] Risk Detected | HR=136, SpO2=91.0, Glu=75
        
        # 1. Prediction Time (Required for Cassandra Timestamp)
        prediction_time = int(time.time() * 1000) 
        
        # 2. Unique Stream ID (Partition Key)
        unique_stream_id = "patient_A"
        
        # 3. Alert Status
        alert_status = "ALERT" if "[⚠ ALERT]" in alert_string else "OK" 
        
        # 4. Extract latest HR/SpO2 values from the string for storage (simplified extraction)
        try:
            # Note: A real system would pass these values through Flink state, not string parsing.
            hr_latest = float(alert_string.split("HR=")[1].split(",")[0])
            spo2_latest = float(alert_string.split("SpO2=")[1].split(",")[0])
        except:
            hr_latest, spo2_latest = 95.0, 98.0 # Fallback 

        # Final output must match the table schema: (long, text, text, float, float)
        return (prediction_time, unique_stream_id, alert_status, hr_latest, spo2_latest)


def create_flink_job():
    print("✅ Starting Flink 2.1 Stream Processor...")

    # 1️⃣ Create Stream Execution Environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # 2️⃣ Configure Kafka Source
    kafka_source = KafkaSource.builder() \
        .set_bootstrap_servers(KAFKA_SERVER) \
        .set_topics(KAFKA_SOURCE_TOPIC) \
        .set_group_id("epilepsy_processor_group") \
        .set_value_only_deserializer(SimpleStringSchema()) \
        .set_starting_offsets(KafkaSource.STARTING_OFFSETS_EARLIEST) \
        .build()

    # 3️⃣ Create DataStream and Parse JSON
    stream = env.from_source(kafka_source, WatermarkStrategy.no_watermarks(), "Epilepsy Kafka Source")
    
    output_types = Types.TUPLE([
        Types.STRING(), Types.STRING(), Types.INT(), Types.FLOAT(), Types.FLOAT(),
        Types.INT(), Types.INT(), Types.INT()
    ])
    
    parsed_stream = stream.map(parse_json, output_type=output_types).name("JSON Parser")
    
    # 4️⃣ Keyed Stream (by unique stream ID)
    keyed_stream = parsed_stream.key_by(lambda x: x[0])

    # 5️⃣ DEMO PREDICTION LOGIC (Multi-Factor Check)
    def multi_factor_risk_check(value):
        # Value tuple: (id, time, hr, spo2, movement, stress, meds, glucose)
        hr, spo2, movement, glucose, meds = value[2], value[3], value[4], value[7], value[6]
        
        is_motor_risk = hr > 130 and movement > 3.0
        is_metabolic_crisis = spo2 < 90.0 and glucose < 70 and meds == 0

        if is_motor_risk or is_metabolic_crisis:
            # ALERT when critical factors align
            return f"[⚠ ALERT] Risk Detected | HR={hr}, SpO2={spo2}, Glu={glucose}"
        else:
            return f"OK | HR={hr}, SpO2={spo2}, Glu={glucose}"

    risk_stream = keyed_stream.map(multi_factor_risk_check).name("Risk Calculator")

    # 6️⃣ SINK 1: Write Results to Cassandra (The Serving Layer)
    CassandraSink.add_sink(risk_stream.map(CassandraMapper(), output_type=Types.TUPLE([
        Types.LONG(), Types.STRING(), Types.STRING(), Types.FLOAT(), Types.FLOAT()
    ]))) \
        .set_query("INSERT INTO risk_monitoring.alerts (prediction_time, unique_stream_id, alert_status, hr_latest, spo2_latest) VALUES (?, ?, ?, ?, ?)") \
        .set_host(CASSANDRA_HOST) \
        .set_port(9042) \
        .set_max_concurrent_requests(500) \
        .build()
    
    # 7️⃣ SINK 2: Output to Console (for debugging/monitoring in Terminal 5)
    risk_stream.print()

    # 8️⃣ Execute the Flink job
    env.execute("Real-Time Seizure Monitoring System")

if __name__ == "__main__":
    create_flink_job()