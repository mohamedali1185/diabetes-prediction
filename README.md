# Diabetes Risk Prediction App

A machine learning web application that predicts an individual's risk of diabetes based on health, lifestyle, and demographic factors.

🔗 **Live app:** [Add your Streamlit Cloud link here]

## Overview

This project uses a CatBoost classification model trained on a large-scale health indicators dataset to estimate diabetes risk from user-provided inputs, including physical activity, diet, sleep, blood pressure, cholesterol, glucose levels, and other health metrics.

## Features

- Interactive web form for entering patient health data
- Real-time risk prediction (high risk / low risk)
- Model trained and compared across multiple algorithms (Logistic Regression, KNN, Decision Tree, Random Forest, SVM, XGBoost, CatBoost)
- Final model: CatBoost, selected for best performance and native categorical feature handling

## Tech Stack

- **Model:** CatBoost (gradient boosting)
- **App framework:** Streamlit
- **Deployment:** Streamlit Community Cloud
- **Data processing:** pandas, scikit-learn

## Project Structure

```
├── app.py                  # Streamlit web application
├── diabetes_model.cbm      # Trained CatBoost model artifact
├── requirements.txt        # Python dependencies
└── README.md
```

## Dataset

[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/mohankrishnathalla/diabetes-health-indicators-dataset/data) — Kaggle, ~100,000 simulated patient records.

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author

Mohamed Ali — Graduation Project, [Your University Name]
