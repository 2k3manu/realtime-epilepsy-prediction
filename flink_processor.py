import json
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common import WatermarkStrategy
from pyflink.datastream.connectors.kafka import KafkaSource
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types

# --- CONFIGURATION ---
KAFKA_SERVER = '127.0.0.1:9092'
KAFKA_SOURCE_TOPIC = 'epilepsy_telemetry'
# ----------------------

def parse_json(json_string):
    """Convert raw Kafka JSON message into tuple of telemetry values"""
    try:
        data = json.loads(json_string)
        return (
            data.get('unique_stream_id'),
            data.get('time'),
            data.get('heart_rate_bpm', 0),
            data.get('spo2_percent', 0.0),
            data.get('movement_g', 0.0),
            data.get('stress_level', 0),
            data.get('medication_taken', 1),
            data.get('blood_glucose_mgdl', 90)
        )
    except Exception as e:
        return ("unknown", "0", 0, 0.0, 0.0, 0, 0, 0)

def create_flink_job():
    print("✅ Starting Flink 2.1 Stream Processor...")

    # 1️⃣ Create Stream Execution Environment
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    # 2️⃣ Configure the new Kafka Source API
    kafka_source = KafkaSource.builder() \
        .set_bootstrap_servers(KAFKA_SERVER) \
        .set_topics(KAFKA_SOURCE_TOPIC) \
        .set_group_id("epilepsy_processor_group") \
        .set_value_only_deserializer(SimpleStringSchema()) \
        .build()

    # 3️⃣ Create DataStream from Kafka Source
    stream = env.from_source(
        kafka_source,
        WatermarkStrategy.no_watermarks(),
        "Epilepsy Kafka Source"
    )

    # 4️⃣ Parse JSON into structured tuples
    parsed_stream = stream.map(
        parse_json,
        output_type=Types.TUPLE([
            Types.STRING(), Types.STRING(),
            Types.INT(), Types.FLOAT(), Types.FLOAT(),
            Types.INT(), Types.INT(), Types.INT()
        ])
    ).name("JSON Parser")

    # 5️⃣ Keyed Stream (by patient ID)
    keyed_stream = parsed_stream.key_by(lambda x: x[0])

    # 6️⃣ Simulated Multi-Factor Risk Evaluation
    def multi_factor_risk_check(value):
        hr, spo2, movement, glucose, meds = value[2], value[3], value[4], value[7], value[6]
        is_motor_risk = hr > 130 and movement > 3.0
        is_metabolic_crisis = spo2 < 90.0 and glucose < 70 and meds == 0

        if is_motor_risk or is_metabolic_crisis:
            return f"[⚠ ALERT] Risk Detected | HR={hr}, SpO2={spo2}, Move={movement}, Glu={glucose}"
        else:
            return f"OK | HR={hr}, SpO2={spo2}, Move={movement}, Glu={glucose}"

    risk_stream = keyed_stream.map(multi_factor_risk_check).name("Risk Calculator")

    # 7️⃣ Output Stream
    risk_stream.print()

    # 8️⃣ Execute the Flink job
    env.execute("Real-Time Seizure Monitoring System")

if __name__ == "__main__":
    create_flink_job()
