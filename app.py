import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostClassifier

model = CatBoostClassifier()
model.load_model("diabetes_model.cbm")


st.title("Diabetes Prediction App")
st.write("Enter patient information below:")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=90, value=70)
    income_level = st.selectbox("Income Level", ["Low", "Lower-Middle", "Middle", "Upper-Middle", "High"], index=0)
    alcohol = st.number_input("Alcohol Consumption (per week)", min_value=0, max_value=30, value=5)
    physical_activity = st.number_input("Physical Activity (min/week)", min_value=0, max_value=600, value=20)
    diet_score = st.number_input("Diet Score (0-10)", min_value=0.0, max_value=10.0, value=1.0)
    sleep_hours = st.number_input("Sleep Hours Per Day", min_value=3.0, max_value=12.0, value=4.0)
    screen_time = st.number_input("Screen Time (hours/day)", min_value=0.0, max_value=12.0, value=10.0)
    family_history = st.selectbox("Family History of Diabetes", [0, 1], index=1, format_func=lambda x: "Yes" if x == 1 else "No")
    hypertension = st.selectbox("Hypertension History", [0, 1], index=1, format_func=lambda x: "Yes" if x == 1 else "No")
    cardiovascular = st.selectbox("Cardiovascular History", [0, 1], index=1, format_func=lambda x: "Yes" if x == 1 else "No")

with col2:
    bmi = st.number_input("BMI", min_value=15.0, max_value=45.0, value=38.0)
    waist_hip = st.number_input("Waist to Hip Ratio", min_value=0.7, max_value=1.2, value=1.1)
    systolic_bp = st.number_input("Systolic BP", min_value=90, max_value=180, value=160)
    diastolic_bp = st.number_input("Diastolic BP", min_value=60, max_value=120, value=100)
    heart_rate = st.number_input("Heart Rate", min_value=50, max_value=120, value=95)
    cholesterol = st.number_input("Total Cholesterol", min_value=120, max_value=300, value=280)
    hdl = st.number_input("HDL Cholesterol", min_value=20, max_value=100, value=25)
    ldl = st.number_input("LDL Cholesterol", min_value=50, max_value=200, value=190)
    triglycerides = st.number_input("Triglycerides", min_value=50, max_value=500, value=450)
    glucose_fasting = st.number_input("Glucose Fasting", min_value=70, max_value=250, value=200)
    glucose_postprandial = st.number_input("Glucose Postprandial", min_value=90, max_value=350, value=300)
    insulin_level = st.number_input("Insulin Level", min_value=2.0, max_value=50.0, value=45.0)

gender = st.selectbox("Gender", ["Male", "Female"], index=0)
ethnicity = st.selectbox("Ethnicity", ["Asian", "Black", "Hispanic", "White"], index=0)
education = st.selectbox("Education Level", ["Graduate", "Highschool", "No formal", "Postgraduate"], index=0)
employment = st.selectbox("Employment Status", ["Employed", "Retired", "Student", "Unemployed"], index=1)
smoking = st.selectbox("Smoking Status", ["Current", "Former", "Never"], index=0)

income_mapping = {"Low": 0, "Lower-Middle": 1, "Middle": 2, "Upper-Middle": 3, "High": 4}

if st.button("Predict"):
    input_dict = {
        "age": age,
        "gender": 1 if gender == "Male" else 0,
        "income_level": income_mapping[income_level],
        "alcohol_consumption_per_week": alcohol,
        "physical_activity_minutes_per_week": physical_activity,
        "diet_score": diet_score,
        "sleep_hours_per_day": sleep_hours,
        "screen_time_hours_per_day": screen_time,
        "family_history_diabetes": family_history,
        "hypertension_history": hypertension,
        "cardiovascular_history": cardiovascular,
        "bmi": bmi,
        "waist_to_hip_ratio": waist_hip,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "heart_rate": heart_rate,
        "cholesterol_total": cholesterol,
        "hdl_cholesterol": hdl,
        "ldl_cholesterol": ldl,
        "triglycerides": triglycerides,
        "glucose_fasting": glucose_fasting,
        "glucose_postprandial": glucose_postprandial,
        "insulin_level": insulin_level,
        "ethnicity_Black": 1 if ethnicity == "Black" else 0,
        "ethnicity_Hispanic": 1 if ethnicity == "Hispanic" else 0,
        "ethnicity_White": 1 if ethnicity == "White" else 0,
        "education_level_Highschool": 1 if education == "Highschool" else 0,
        "education_level_No formal": 1 if education == "No formal" else 0,
        "education_level_Postgraduate": 1 if education == "Postgraduate" else 0,
        "employment_status_Retired": 1 if employment == "Retired" else 0,
        "employment_status_Student": 1 if employment == "Student" else 0,
        "employment_status_Unemployed": 1 if employment == "Unemployed" else 0,
        "smoking_status_Former": 1 if smoking == "Former" else 0,
        "smoking_status_Never": 1 if smoking == "Never" else 0,
    }

    input_df = pd.DataFrame([input_dict])
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ High risk of Diabetes detected.")
    else:
        st.success("✅ Low risk of Diabetes.")