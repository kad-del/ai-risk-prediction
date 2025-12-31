import streamlit as st
import joblib
import pandas as pd

model = joblib.load("risk_model.pkl")

st.title("Crowd & Traffic Risk Prediction 🚦")

day = st.selectbox("Day Type", ["Weekday", "Weekend"])
time = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])

day_val = 0 if day == "Weekday" else 1
time_val = {"Morning": 0, "Afternoon": 1, "Evening": 2}[time]
traffic_val = {"Low": 0, "Medium": 1, "High": 2}[traffic]
import pandas as pd

input_data = pd.DataFrame(
    [[crowd, traffic, weather, time]],
    columns=["crowd_density", "traffic_level", "weather", "time"]
)

prediction = model.predict(input_data)[0]

