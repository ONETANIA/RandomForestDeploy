import streamlit as st
import numpy as np
from prediction import predict_diabetes

st.set_page_config(page_title="Diabetes Predictor", layout="wide")

st.title("🩺 Diabetes Risk Prediction")
st.write("Model Machine Learning menggunakan Random Forest dengan custom threshold.")
st.divider()

st.subheader("Masukkan Data Pengguna")
st.write("Jawab sesuai kondisi Anda. Semua pertanyaan berdasarkan survei BRFSS (CDC).")

col1, col2 = st.columns(2)

# ==========================
# KOLOM 1
# ==========================
with col1:

    HighBP = st.selectbox(
        "Tekanan darah tinggi?",
        ["Tidak", "Ya"]
    )

    HighChol = st.selectbox(
        "Kolesterol tinggi?",
        ["Tidak", "Ya"]
    )

    BMI = st.slider("Indeks Massa Tubuh (BMI)", 10, 60, 25)

    Age = st.selectbox(
        "Kategori usia",
        options=list(range(1, 13 + 1)),
        format_func=lambda x: {
            1: "18–24",
            2: "25–29",
            3: "30–34",
            4: "35–39",
            5: "40–44",
            6: "45–49",
            7: "50–54",
            8: "55–59",
            9: "60–64",
            10: "65–69",
            11: "70–74",
            12: "75–79",
            13: "80+"
        }[x]
    )

    PhysHlth = st.slider(
        "Hari kesehatan fisik buruk (0–30)",
        0, 30, 5
    )

# ==========================
# KOLOM 2
# ==========================
with col2:

    GenHlth = st.selectbox(
        "Penilaian kesehatan umum",
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: {
            1: "Excellent",
            2: "Very Good",
            3: "Good",
            4: "Fair",
            5: "Poor"
        }[x]
    )

    MentHlth = st.slider(
        "Hari kesehatan mental buruk (0–30)",
        0, 30, 3
    )

    Education = st.selectbox(
        "Tingkat pendidikan",
        options=[1, 2, 3, 4, 5, 6],
        format_func=lambda x: {
            1: "Tidak sekolah",
            2: "SD",
            3: "SMP",
            4: "SMA",
            5: "Kuliah sebagian",
            6: "Lulus kuliah"
        }[x]
    )

    Income = st.selectbox(
        "Pendapatan Tahunan",
        options=[1,2,3,4,5,6,7,8],
        format_func=lambda x: {
            1: "< $10.000",
            2: "$10.000 – $14.999",
            3: "$15.000 – $19.999",
            4: "$20.000 – $24.999",
            5: "$25.000 – $34.999",
            6: "$35.000 – $49.999",
            7: "$50.000 – $74.999",
            8: "≥ $75.000"
        }[x]
    )

    Smoker = st.selectbox(
        "Pernah merokok ≥ 100 batang?",
        ["Tidak", "Ya"]
    )

# ==========================
# KONVERSI INPUT USER
# ==========================

user_input = {
    "BMI": BMI,
    "Age": Age,
    "Income": Income,
    "PhysHlth": PhysHlth,
    "Education": Education,
    "GenHlth": GenHlth,
    "MentHlth": MentHlth,
    "HighBP": 1 if HighBP == "Ya" else 0,
    "HighChol": 1 if HighChol == "Ya" else 0,
    "Smoker": 1 if Smoker == "Ya" else 0,
    "Fruits": 0,  # default
}

st.divider()

# ==========================
# PREDIKSI
# ==========================

if st.button("Prediksi"):
    label, prob = predict_diabetes(user_input)

    st.success(f"🎯 **Hasil Prediksi: {label}**")
    st.write(f"Probabilitas diabetes: **{prob:.4f}**")
