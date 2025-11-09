from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer
from pyflink.common.serialization import SimpleStringSchema
import json, cassandra.cluster as cc

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

consumer = FlinkKafkaConsumer(
    topics='epilepsy_telemetry',
    deserialization_schema=SimpleStringSchema(),
    properties={'bootstrap.servers': 'localhost:9092', 'group.id': 'flink-group'}
)

stream = env.add_source(consumer)

def process_data(value):
    try:
        data = json.loads(value)
        cluster = cc.Cluster(['127.0.0.1'])
        session = cluster.connect('epilepsy_monitoring')

        query = """
        INSERT INTO vitals_data (
            patient_id, timestamp, heart_rate_bpm, spo2_percent, body_temperature_c,
            movement_g, stress_level, blood_glucose_mgdl, sleep_hours, noise_exposure_db,
            ambient_light_lux, seizure_label, risk_level
        ) VALUES (%(patient_id)s, toTimestamp(now()), %(heart_rate_bpm)s, %(spo2_percent)s,
        %(body_temperature_c)s, %(movement_g)s, %(stress_level)s, %(blood_glucose_mgdl)s,
        %(sleep_hours)s, %(noise_exposure_db)s, %(ambient_light_lux)s, %(seizure_label)s,
        %(risk_level)s)
        """
        session.execute(query, data)
        print(f"✅ Inserted into Cassandra: {data}")
    except Exception as e:
        print("❌ Error:", e)

stream.map(process_data)
env.execute("Epilepsy-Flink-Stream")
