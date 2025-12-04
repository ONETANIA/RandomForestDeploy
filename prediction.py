import joblib
import gzip
import json
import numpy as np

# Load model
with gzip.open("model.sav.gz", "rb") as f:
    model = joblib.load(f)

# Load scaler (not gzipped)
scaler = joblib.load("scaler.sav")

# Load feature order
with open("features.json", "r") as f:
    selected_features = json.load(f)

# Load threshold
with open("threshold.txt", "r") as f:
    threshold = float(f.read().strip())


def predict_diabetes(user_input_dict):

    # Pastikan urutan fitur sama seperti training
    values = [user_input_dict[f] for f in selected_features]

    X = np.array(values).reshape(1, -1)

    X_scaled = scaler.transform(X)

    prob = model.predict_proba(X_scaled)[0, 1]

    label = 1 if prob >= threshold else 0

    return label, prob
