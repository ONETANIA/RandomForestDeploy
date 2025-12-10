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
        "Kategori usia (1=18–24, 2=25–29, 3=30–34, ..., 13=80+)",
        1, 13, 5
    )

    PhysHlth = st.slider(
        "Dalam 30 hari terakhir, berapa hari kesehatan fisik Anda
