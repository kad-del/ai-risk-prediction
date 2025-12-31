import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("risk_model.pkl")

# Title
st.title("SAFEROUTE AI-Crowd & Traffic Risk Prediction 🚦")

# Inputs
day = st.selectbox("Day Type", ["Weekday", "Weekend"])
time = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])

# Encoding
day_val = 0 if day == "Weekday" else 1
time_val = {"Morning": 0, "Afternoon": 1, "Evening": 2}[time]
traffic_val = {"Low": 0, "Medium": 1, "High": 2}[traffic]

# Prediction
if st.button("Predict Risk"):
    input_data = np.array([[day_val, time_val, traffic_val]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Risk Level: {prediction}")
