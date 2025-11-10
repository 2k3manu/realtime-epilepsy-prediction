from flask import Flask, jsonify
from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import joblib
import numpy as np
import pandas as pd

# ---------------------------
#  Flask App Initialization
# ---------------------------
app = Flask(__name__)

# ---------------------------
#  Cassandra Connection
# ---------------------------
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('epilepsy_monitoring')
session.row_factory = dict_factory

# ---------------------------
#  Load Trained Models
# ---------------------------
rf_risk_model = joblib.load("../rf_risk_model.joblib")
rf_seizure_model = joblib.load("../rf_seizure_model.joblib")
scaler = joblib.load("../scaler.joblib")
label_encoder = joblib.load("../label_encoder.joblib")

print("✅ Models loaded successfully")

# ---------------------------
#  API Endpoint: Predict
# ---------------------------
@app.route('/predict', methods=['GET'])
def predict_latest():
    query = "SELECT * FROM vitals_data LIMIT 1;"
    rows = session.execute(query)
    latest = list(rows)[0] if rows else None

    if not latest:
        return jsonify({"message": "No data found in Cassandra."}), 404

    # Convert to DataFrame for consistency
    df = pd.DataFrame([latest])

    # Extract required features for ML model
    feature_cols = [
        'heart_rate_bpm', 'spo2_percent', 'body_temperature_c', 'movement_g',
        'stress_level', 'blood_glucose_mgdl', 'sleep_hours',
        'noise_exposure_db', 'ambient_light_lux'
    ]

    X = df[feature_cols]
    X_scaled = scaler.transform(X)

    # Perform predictions
    risk_pred = rf_risk_model.predict(X_scaled)[0]
    seizure_pred = rf_seizure_model.predict(X_scaled)[0]

    # Decode labels
    risk_label = label_encoder.inverse_transform([risk_pred])[0]
    seizure_label = int(seizure_pred)

    response = {
        "patient_id": latest['patient_id'],
        "heart_rate_bpm": latest['heart_rate_bpm'],
        "spo2_percent": latest['spo2_percent'],
        "body_temperature_c": latest['body_temperature_c'],
        "movement_g": latest['movement_g'],
        "stress_level": latest['stress_level'],
        "blood_glucose_mgdl": latest['blood_glucose_mgdl'],
        "sleep_hours": latest['sleep_hours'],
        "noise_exposure_db": latest['noise_exposure_db'],
        "ambient_light_lux": latest['ambient_light_lux'],
        "predicted_risk_level": risk_label,
        "predicted_seizure_label": seizure_label
    }

    return jsonify(response)

# ---------------------------
#  Run Flask App
# ---------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
