# 🌾 Crop Irrigation Need Predictor

A machine learning web app that predicts whether a crop's irrigation need is **Low**, **Medium**, or **High** based on soil, weather, and crop conditions.

## Live Demo
🔗 [Add your Streamlit Cloud link here]

## Overview

Farmers and agricultural planners can input field conditions and instantly get an irrigation recommendation — no manual analysis needed.

## Features

- Predicts irrigation need across 3 levels: Low, Medium, High
- Takes 19 input features including soil type, weather, crop type, and region
- 98.37% accuracy on validation set (630,000 rows)
- Clean 3-column input layout
- Instant predictions with color-coded results

## Model Details

- **Algorithm:** XGBoost Classifier
- **Preprocessing:** OneHotEncoding + sklearn Pipeline
- **Training Data:** Kaggle Playground Series S6E4
- **Accuracy:** 98.37%
- **Target Classes:** Low, Medium, High irrigation need

## Input Features

| Feature | Type |
|---|---|
| Soil Type | Categorical |
| Soil pH | Numerical |
| Soil Moisture | Numerical |
| Organic Carbon | Numerical |
| Electrical Conductivity | Numerical |
| Temperature (°C) | Numerical |
| Humidity | Numerical |
| Rainfall (mm) | Numerical |
| Sunlight Hours | Numerical |
| Wind Speed (km/h) | Numerical |
| Crop Type | Categorical |
| Crop Growth Stage | Categorical |
| Season | Categorical |
| Irrigation Type | Categorical |
| Water Source | Categorical |
| Field Area (hectares) | Numerical |
| Mulching Used | Categorical |
| Previous Irrigation (mm) | Numerical |
| Region | Categorical |

## Tech Stack

- Python
- Streamlit
- XGBoost
- Scikit-learn
- Pandas
- Joblib

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Project Structure

```
irrigation-predictor/
├── app.py
├── irrigation_model.pkl
├── requirements.txt
└── README.md
```
