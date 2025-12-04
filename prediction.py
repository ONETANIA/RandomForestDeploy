import json
import numpy as np
import joblib
import gzip

# MODEL
with gzip.open("model.sav.gz", "rb") as f:
    model = joblib.load(f)

# SCALER (tidak gzip)
scaler = joblib.load("scaler.sav")

# FEATURES
with open("features.json", "r") as f:
    selected_features = json.load(f)

# THRESHOLD
with open("threshold.txt", "r") as f:
    threshold = float(f.read().strip())



def predict_diabetes(user_input_dict):
    """
    user_input_dict = dict 10 fitur sesuai feature_order
    """

    # Ubah dictionary ke list sesuai urutan fitur model
    values = [user_input_dict[f] for f in feature_order]
    X = np.array([values])

    # Scaling
    X_scaled = scaler.transform(X)

    # Probabilitas kelas 1 (diabetes)
    prob = model.predict_proba(X_scaled)[0][1]

    # Custom threshold
    pred = int(prob >= threshold)

    label = "Diabetes" if pred == 1 else "Tidak Diabetes"

    return label, float(prob)

