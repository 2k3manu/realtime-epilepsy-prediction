from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load trained models and tools
rf_risk = joblib.load("rf_risk_model.joblib")
rf_seizure = joblib.load("rf_seizure_model.joblib")
scaler = joblib.load("scaler.joblib")
label_encoder = joblib.load("label_encoder.joblib")

@app.route("/")
def index():
    return jsonify({"message": "🧠 AI Seizure Prediction API Active"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        # Expected input fields
        expected_features = [
            "heart_rate_bpm", "spo2_percent", "body_temperature_c", "movement_g",
            "stress_level", "blood_glucose_mgdl", "sleep_hours",
            "noise_exposure_db", "ambient_light_lux"
        ]

        # Ensure all fields are present
        if not all(f in data for f in expected_features):
            return jsonify({"error": f"Missing required features: {expected_features}"}), 400

        # Convert input to DataFrame
        input_df = pd.DataFrame([data])[expected_features]

        # Scale data
        scaled = scaler.transform(input_df)

        # Predict
        risk_pred = rf_risk.predict(scaled)
        seizure_pred = rf_seizure.predict(scaled)

        risk_label = label_encoder.inverse_transform(risk_pred)[0]
        seizure_label = int(seizure_pred[0])

        return jsonify({
            "risk_level": risk_label,
            "seizure_label": seizure_label,
            "status": "Prediction successful ✅"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
