import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_seizure_dataset():
    """
    Generates a synthetic, comprehensive dataset for real-time epileptic seizure prediction.
    It includes 10 physiological/behavioral features and a seizure label (11,700 rows).
    """
    N_ROWS = 12000
    SEIZURE_PROB = 0.025  # 2.5% of data labeled as seizure
    SEIZURE_PERIOD = 20 # Seizure event lasts 20 rows (10 minutes)
    N_SEIZURES_TOTAL = int(N_ROWS * SEIZURE_PROB)
    N_NON_SEIZURES = N_ROWS - N_SEIZURES_TOTAL
    N_PATIENTS = 5 

    start_time = datetime.now() - timedelta(days=25)
    time_stamps = [start_time + timedelta(minutes=0.5 * i) for i in range(N_ROWS)]
    patient_ids = [f'patient_{i+1}' for i in np.random.choice(N_PATIENTS, size=N_ROWS)]

    # --- Generate Non-Seizure Data (Normal Distribution) ---
    df_non_seizure = pd.DataFrame({
        'time': time_stamps[:N_NON_SEIZURES],
        'patient_id': patient_ids[:N_NON_SEIZURES],
        'seizure_label': 0
    })

    # Normal Ranges:
    df_non_seizure['heart_rate_bpm'] = np.random.normal(loc=75, scale=8, size=N_NON_SEIZURES).clip(60, 100).astype(int)
    df_non_seizure['movement_g'] = np.random.normal(loc=0.8, scale=0.3, size=N_NON_SEIZURES).clip(0.1, 1.5).round(2)
    df_non_seizure['temperature_c'] = np.random.normal(loc=36.8, scale=0.3, size=N_NON_SEIZURES).clip(36.0, 37.5).round(2)
    df_non_seizure['spo2_percent'] = np.random.normal(loc=98.5, scale=1.0, size=N_NON_SEIZURES).clip(95, 100).round(1)
    df_non_seizure['eda_microsiemens'] = np.random.normal(loc=2.5, scale=1.0, size=N_NON_SEIZURES).clip(0.5, 5.0).round(2)
    df_non_seizure['sleep_hours'] = np.random.normal(loc=7.0, scale=1.5, size=N_NON_SEIZURES).clip(4, 10).round(1)
    df_non_seizure['stress_level'] = np.random.normal(loc=30, scale=15, size=N_NON_SEIZURES).clip(0, 70).astype(int)
    df_non_seizure['medication_taken'] = np.random.choice([0, 1], size=N_NON_SEIZURES, p=[0.1, 0.9])
    df_non_seizure['ambient_light_lux'] = np.random.normal(loc=200, scale=150, size=N_NON_SEIZURES).clip(10, 800).astype(int)
    df_non_seizure['blood_glucose_mgdl'] = np.random.normal(loc=95, scale=15, size=N_NON_SEIZURES).clip(70, 140).astype(int)

    # --- Generate Seizure Data (Extreme/Anomalous Values) ---
    seizure_data = []
    for _ in range(N_SEIZURES_TOTAL // SEIZURE_PERIOD):
        patient_id = np.random.choice(patient_ids)
        event_start_time = df_non_seizure['time'].sample(1).iloc[0]
        seizure_time_stamps = [event_start_time + timedelta(minutes=0.5 * i) for i in range(SEIZURE_PERIOD)]

        seizure_block = pd.DataFrame({
            'time': seizure_time_stamps,
            'patient_id': [patient_id] * SEIZURE_PERIOD,
            'seizure_label': [1] * SEIZURE_PERIOD,
            
            # Anomalous Ranges (Triggers):
            'heart_rate_bpm': np.random.normal(loc=135, scale=10, size=SEIZURE_PERIOD).clip(120, 160).astype(int),
            'movement_g': np.random.normal(loc=4.0, scale=0.5, size=SEIZURE_PERIOD).clip(2.5, 5.0).round(2),
            'temperature_c': np.random.normal(loc=38.5, scale=0.3, size=SEIZURE_PERIOD).clip(37.8, 39.5).round(2),
            'spo2_percent': np.random.normal(loc=90, scale=2.0, size=SEIZURE_PERIOD).clip(85, 95).round(1),
            'eda_microsiemens': np.random.normal(loc=10.0, scale=2.0, size=SEIZURE_PERIOD).clip(6.0, 15.0).round(2),
            'sleep_hours': np.random.normal(loc=4.0, scale=1.0, size=SEIZURE_PERIOD).clip(2, 6).round(1), 
            'stress_level': np.random.normal(loc=90, scale=5, size=SEIZURE_PERIOD).clip(80, 100).astype(int), 
            'medication_taken': np.random.choice([0], size=SEIZURE_PERIOD), 
            'ambient_light_lux': np.random.normal(loc=500, scale=100, size=SEIZURE_PERIOD).clip(300, 700).astype(int), 
            'blood_glucose_mgdl': np.random.normal(loc=65, scale=5, size=SEIZURE_PERIOD).clip(50, 75).astype(int)
        })
        seizure_data.append(seizure_block)

    df_seizure = pd.concat(seizure_data, ignore_index=True)

    # --- Combine and Finalize ---
    df = pd.concat([df_non_seizure.iloc[:N_NON_SEIZURES - len(df_seizure)], df_seizure], ignore_index=True)
    df = df.sample(frac=1).reset_index(drop=True)

    df = df.head(11700) 
    column_order = ['time', 'patient_id', 'heart_rate_bpm', 'movement_g', 'temperature_c', 
                    'spo2_percent', 'eda_microsiemens', 'sleep_hours', 'stress_level', 
                    'medication_taken', 'ambient_light_lux', 'blood_glucose_mgdl', 'seizure_label']
    df = df[column_order]

    output_filename = 'patient_seizure_dataset.csv'
    df.to_csv(output_filename, index=False)
    return f"Dataset successfully generated and saved as {output_filename} with {len(df)} records."

if __name__ == "__main__":
    result_message = generate_seizure_dataset()
    print(result_message)
    print("\n-----------------------------------------------------------------------")
    print("ACTION REQUIRED: Now run the Python Producer script in a new terminal:")
    print("python data_generator.py")
    print("-----------------------------------------------------------------------")