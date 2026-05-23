import streamlit as st
import joblib
import numpy as np

# Page Config
st.set_page_config(
    page_title="ML Project",
    page_icon="✨"
)

# Title
st.title("ML Project using Python")

# Load Model
try:
    lin_model = joblib.load('linear_model.joblib')
    st.success("✅ Model loaded successfully")

except FileNotFoundError:
    st.error("❌ linear_model.joblib file not found!")
    st.info("👉 Pehle model.ipynb run karo")
    st.stop()

# User Input
user_input = st.number_input(
    "Experience Years",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1
)

# Prediction Button
if st.button("Predict Salary"):

    input_data = np.array([[user_input]])

    prediction = lin_model.predict(input_data)[0]

    st.success(f"💰 Predicted Salary: ${prediction:,.2f}")