import joblib
import json
import numpy as np
import pandas as pd
import streamlit as st

# Load model and label map
pipeline = joblib.load("irrigation_model.pkl")
reverse_map = {0: "Low", 1: "Medium", 2: "High"}
st.set_page_config(page_title="🌾 Irrigation Need Predictor", layout="wide")
st.title("🌾 Crop Irrigation Need Predictor")
st.caption("Predicts whether irrigation need is Low, Medium, or High")

# ── Inputs ──────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    soil_type = st.selectbox("Soil Type", ["Loamy", "Clay", "Sandy", "Silt"])
    soil_ph = st.slider("Soil pH", 3.0, 10.0, 6.5)
    soil_moisture = st.slider("Soil Moisture", 0.0, 100.0, 30.0)
    organic_carbon = st.slider("Organic Carbon", 0.0, 3.0, 1.0)
    electrical_conductivity = st.slider("Electrical Conductivity", 0.0, 5.0, 2.0)

with col2:
    temperature = st.slider("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.slider("Humidity (%)", 0.0, 100.0, 60.0)
    rainfall = st.slider("Rainfall (mm)", 0.0, 3000.0, 500.0)
    sunlight_hours = st.slider("Sunlight Hours", 0.0, 15.0, 7.0)
    wind_speed = st.slider("Wind Speed (km/h)", 0.0, 50.0, 10.0)

with col3:
    crop_type = st.selectbox("Crop Type", ["Sugarcane", "Wheat", "Rice", "Potato", "Cotton", "Maize"])
    crop_stage = st.selectbox("Crop Growth Stage", ["Sowing", "Vegetative", "Flowering", "Harvest"])
    season = st.selectbox("Season", ["Zaid", "Kharif", "Rabi"])
    irrigation_type = st.selectbox("Irrigation Type", ["Drip", "Rainfed", "Sprinkler", "Canal"])
    water_source = st.selectbox("Water Source", ["Rainwater", "River", "Reservoir", "Groundwater"])
    field_area = st.slider("Field Area (hectares)", 0.0, 20.0, 5.0)
    mulching = st.selectbox("Mulching Used", ["No", "Yes"])
    prev_irrigation = st.slider("Previous Irrigation (mm)", 0.0, 200.0, 80.0)
    region = st.selectbox("Region", ["East", "South", "North", "West", "Central"])

# ── Predict ──────────────────────────────────────────────────────
if st.button("🔍 Predict Irrigation Need", use_container_width=True):
    input_df = pd.DataFrame([{
        "id": 0,
        "Soil_Type": soil_type,
        "Soil_pH": soil_ph,
        "Soil_Moisture": soil_moisture,
        "Organic_Carbon": organic_carbon,
        "Electrical_Conductivity": electrical_conductivity,
        "Temperature_C": temperature,
        "Humidity": humidity,
        "Rainfall_mm": rainfall,
        "Sunlight_Hours": sunlight_hours,
        "Wind_Speed_kmh": wind_speed,
        "Crop_Type": crop_type,
        "Crop_Growth_Stage": crop_stage,
        "Season": season,
        "Irrigation_Type": irrigation_type,
        "Water_Source": water_source,
        "Field_Area_hectare": field_area,
        "Mulching_Used": mulching,
        "Previous_Irrigation_mm": prev_irrigation,
        "Region": region,
    }])

    pred = pipeline.predict(input_df)[0]
    result = reverse_map[pred]

    if result == "Low":
        st.success("💧 Irrigation Need: **Low**")
    elif result == "Medium":
        st.warning("💧 Irrigation Need: **Medium**")
    else:
        st.error("💧 Irrigation Need: **High**")
