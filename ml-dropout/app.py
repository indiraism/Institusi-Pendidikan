import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import pickle

# --- Load Model dan Scaler ---
model = pickle.load(open(Path(__file__).parent / "model.pkl", "rb"))
scaler = pickle.load(open(Path(__file__).parent / "scaler.pkl", "rb"))

st.set_page_config(page_title="Batch Prediksi Dropout", layout="centered")
st.title("📂 Prediksi Dropout Siswa - Upload CSV")

st.markdown("""
Unggah file **CSV** yang berisi 36 fitur lengkap (tanpa kolom target).
Model akan memproses seluruh baris untuk memprediksi risiko dropout.
""")

# --- Upload File CSV ---
uploaded_file = st.file_uploader("Unggah file CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # --- Cek apakah jumlah kolom sesuai ---
        if df.shape[1] != 36:
            st.warning(f"⚠️ File Anda memiliki {df.shape[1]} kolom. Harusnya 36 kolom sesuai model.")
        else:
            st.success("✅ File berhasil diunggah dan dibaca.")
            st.dataframe(df.head())

            # --- Prediksi ---
            X_scaled = scaler.transform(df)
            preds = model.predict(X_scaled)

            # Mapping label ke string
            label_map = {0: "Enrolled", 1: "Internally Transferred", 2: "Dropout"}
            df['Prediksi'] = [label_map[p] for p in preds]

            st.subheader("📊 Hasil Prediksi")
            st.dataframe(df[['Prediksi']].join(df.drop(columns='Prediksi')))

            # --- Download hasil ---
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "⬇️ Unduh Hasil Prediksi",
                data=csv,
                file_name="hasil_prediksi_dropout.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
