import streamlit as st
import numpy as np
import joblib

# Cargar modelo
model = joblib.load("model/fire_model.pkl")

st.set_page_config(page_title="Riesgo de Incendios", layout="centered")
st.title("🔥 Predicción de Riesgo de Incendio Forestal en Bolivia")

st.markdown("""
Este modelo usa variables climáticas y ambientales para predecir el riesgo de incendio.
""")

# Entradas del usuario
temp = st.slider("🌡️ Temperatura (°C)", 10.0, 45.0, 30.0)
humidity = st.slider("💧 Humedad (%)", 0.0, 100.0, 40.0)
wind = st.slider("💨 Viento (km/h)", 0.0, 20.0, 5.0)
precip = st.slider("🌧️ Precipitación (mm)", 0.0, 20.0, 2.0)
ndvi = st.slider("🌿 NDVI (Índice de Vegetación)", 0.0, 1.0, 0.5)

# Botón de predicción
if st.button("Predecir riesgo"):
    input_array = np.array([[temp, humidity, wind, precip, ndvi]])
    prob = model.predict_proba(input_array)[0][1]
    riesgo = "🔥 ALTO" if prob > 0.7 else "🟠 MEDIO" if prob > 0.4 else "🟢 BAJO"
    st.subheader(f"Riesgo estimado: {riesgo}")
    st.write(f"Probabilidad de incendio: **{round(prob * 100, 2)}%**")
