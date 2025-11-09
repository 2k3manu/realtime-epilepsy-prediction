from kafka import KafkaProducer
import json, time, random, datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    heart_rate = random.randint(55, 140)
    spo2 = round(random.uniform(85, 100), 2)
    temp = round(random.uniform(36, 39), 2)
    move = round(random.uniform(0, 4), 2)
    stress = random.randint(1, 10)
    glucose = random.randint(65, 160)
    sleep = round(random.uniform(6, 9), 1)
    noise = round(random.uniform(20, 70), 2)
    light = round(random.uniform(100, 500), 2)
    seizure = 1 if random.random() < 0.2 else 0

    risk = "Normal"
    if heart_rate > 120 or spo2 < 90 or temp > 38.0 or stress > 8 or glucose < 70:
        risk = "High"
    elif heart_rate > 100 or stress > 6 or temp > 37.5:
        risk = "Moderate"

    data = {
        "patient_id": "patient_1",
        "timestamp": datetime.datetime.now().isoformat(),
        "heart_rate_bpm": heart_rate,
        "spo2_percent": spo2,
        "body_temperature_c": temp,
        "movement_g": move,
        "stress_level": stress,
        "blood_glucose_mgdl": glucose,
        "sleep_hours": sleep,
        "noise_exposure_db": noise,
        "ambient_light_lux": light,
        "seizure_label": seizure,
        "risk_level": risk
    }
    return data

while True:
    msg = generate_data()
    producer.send("epilepsy_telemetry", msg)
    print(f"📤 Sent to Kafka: {msg}")
    time.sleep(5)
