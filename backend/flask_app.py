from flask import Flask, jsonify
from cassandra.cluster import Cluster

app = Flask(__name__)

# Cassandra Configuration
CASSANDRA_HOSTS = ['127.0.0.1']
KEYSPACE = 'epilepsy_monitoring'

# Connect to Cassandra
cluster = Cluster(CASSANDRA_HOSTS)
session = cluster.connect(KEYSPACE)


@app.route('/')
def home():
    return jsonify({"message": "Epileptic Seizure Monitoring API Running"})


@app.route('/api/vitals')
def get_latest_vitals():
    """
    Fetch the most recent full record of patient vitals from Cassandra.
    """
    try:
        query = "SELECT * FROM vitals_data LIMIT 1;"
        result = session.execute(query)
        row = result.one()

        if row:
            data = {
                "timestamp": str(row.timestamp),
                "heart_rate_bpm": row.heart_rate_bpm,
                "spo2_percent": row.spo2_percent,
                "body_temperature_c": row.body_temperature_c,
                "movement_g": row.movement_g,
                "stress_level": row.stress_level,
                "blood_glucose_mgdl": row.blood_glucose_mgdl,
                "medication_taken": row.medication_taken,
                "sleep_hours": row.sleep_hours,
                "noise_exposure_db": row.noise_exposure_db,
                "ambient_light_lux": row.ambient_light_lux,
                "seizure_label": row.seizure_label,
                "risk_level": row.risk_level
            }
        else:
            data = {"message": "No data found in vitals_data table."}

    except Exception as e:
        data = {"error": str(e)}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
