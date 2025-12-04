import streamlit as st
import numpy as np
from prediction import predict_diabetes

st.set_page_config(page_title="Diabetes Predictor", layout="wide")

st.title("🩺 Diabetes Risk Prediction")
st.write("Model ML menggunakan Random Forest dengan custom threshold.")

st.divider()

# ==========================
# INPUT USER
# ==========================

st.subheader("Masukkan Data Pengguna")

col1, col2 = st.columns(2)

with col1:
    HighBP = st.selectbox("High BP (0 = no, 1 = yes)", [0, 1])
    HighChol = st.selectbox("High Cholesterol (0 = no, 1 = yes)", [0, 1])
    BMI = st.slider("BMI", 10, 60, 25)
    Age = st.slider("Age category (1–13)", 1, 13, 5)
    PhysHlth = st.slider("Physical Health (0–30 days)", 0, 30, 5)

with col2:
    GenHlth = st.slider("General Health (1=excellent, 5=poor)", 1, 5, 3)
    MentHlth = st.slider("Mental Health (0–30 days)", 0, 30, 3)
    Education = st.slider("Education (1–6)", 1, 6, 3)
    Income = st.slider("Income level (1–8)", 1, 8, 4)
    Smoker = st.selectbox("Smoker? (0=no, 1=yes)", [0, 1])

# Dictionary input sesuai feature_order JSON
user_input = {
    "BMI": BMI,
    "Age": Age,
    "Income": Income,
    "PhysHlth": PhysHlth,
    "Education": Education,
    "GenHlth": GenHlth,
    "MentHlth": MentHlth,
    "HighBP": HighBP,
    "Fruits": 0,  # kalau tidak ada, isi default
    "Smoker": Smoker
}

# Kamu bisa sesuaikan untuk fitur lengkap ya!
# Pastikan sesuai feature_order

st.divider()

if st.button("Prediksi"):
    label, prob = predict_diabetes(user_input)

    st.success(f"**Hasil Prediksi: {label}**")
    st.write(f"Probabilitas diabetes: **{prob:.4f}**")
