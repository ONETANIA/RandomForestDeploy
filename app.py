import streamlit as st
import numpy as np
from prediction import predict_diabetes

st.set_page_config(page_title="Diabetes Predictor", layout="wide")

st.title("🩺 Diabetes Risk Prediction")
st.write("Model Machine Learning menggunakan Random Forest dengan custom threshold.")

st.divider()

# ==========================
# INPUT USER
# ==========================

st.subheader("Masukkan Data Pengguna")
st.write("Isi berdasarkan kondisi kesehatan Anda. Semua pertanyaan berasal dari survei kesehatan BRFSS (CDC).")

col1, col2 = st.columns(2)

# ==========================
# KOLOM 1
# ==========================
with col1:

    HighBP = st.selectbox(
        "Apakah Anda pernah diberitahu oleh tenaga medis bahwa Anda memiliki tekanan darah tinggi? (0 = tidak, 1 = ya)",
        [0, 1]
    )

    HighChol = st.selectbox(
        "Apakah Anda pernah diberitahu oleh tenaga medis bahwa kolesterol Anda tinggi? (0 = tidak, 1 = ya)",
        [0, 1]
    )

    BMI = st.slider(
        "Indeks Massa Tubuh (BMI)",
        10, 60, 25
    )

    Age = st.slider(
        "Kategori usia (1 = 18–24, 2 = 25–29, 3 = 30–34, 4 = 35-39, 5 = 40-44, 6 = 45-49, 7 = 50-54, 8 = 55-59, 9 = 60-64, 10 = 65-69, 11 = 70-74, 12 = 75-79, 13 = 80+)",
        1, 13, 5
    )

    PhysHlth = st.slider(
        "Dalam 30 hari terakhir, berapa hari kesehatan fisik Anda tidak baik? (0–30 hari)",
        0, 30, 5
    )

# ==========================
# KOLOM 2
# ==========================
with col2:

    GenHlth = st.slider(
        "Penilaian kesehatan secara umum (1=excellent, 5=poor)",
        1, 5, 3
    )

    MentHlth = st.slider(
        "Dalam 30 hari terakhir, berapa hari kesehatan mental Anda tidak baik? (0–30 hari)",
        0, 30, 3
    )

    Education = st.slider(
        "Tingkat pendidikan (1=tidak sekolah, 2=SD, 3=SMP, 4=SMA, 5=kuliah sebagian, 6=lulus kuliah)",
        1, 6, 3
    )

    Income = st.slider(
        "Level pendapatan (1=<10k USD, 2=10–15k, ..., 8=>75k USD per tahun)",
        1, 8, 4
    )

    Smoker = st.selectbox(
        "Apakah Anda pernah merokok ≥ 100 batang sepanjang hidup Anda? (0 = tidak, 1 = ya)",
        [0, 1]
    )

# ==========================
# MAKE INPUT DICT
# ==========================

user_input = {
    "BMI": BMI,
    "Age": Age,
    "Income": Income,
    "PhysHlth": PhysHlth,
    "Education": Education,
    "GenHlth": GenHlth,
    "MentHlth": MentHlth,
    "HighBP": HighBP,
    "Smoker": Smoker,
    "Fruits": 0,  # default karena tidak dipakai
}

st.divider()

# ==========================
# PREDIKSI
# ==========================

if st.button("Prediksi"):
    label, prob = predict_diabetes(user_input)

    st.success(f"🎯 **Hasil Prediksi: {label}**")
    st.write(f"Probabilitas diabetes: **{prob:.4f}**")
