# Student Performance Prediction using Machine Learning

## Project Overview

This project predicts a student's final academic grade (G3) using machine learning techniques.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit
- Jupyter Notebook

## Machine Learning Model

Random Forest Regressor is used to predict the final student grade.

## Input Features

- Age
- Study Time
- Past Failures
- Absences
- First Period Grade (G1)
- Second Period Grade (G2)

## Output

The application predicts the student's final grade (G3) on a scale of 0–20.

## Application

A Streamlit web application is provided for interactive prediction.

## Model Performance

The Random Forest model achieved the following results on the test dataset:

- MAE: 1.17
- RMSE: 1.97
- R² Score: 0.81

The model explains approximately 81% of the variation in the final student grades.

## Live Application

The project is deployed using Streamlit Community Cloud.

[Open Live App](https://student-performance-prediction-arundhati777.streamlit.app/)
## How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Student_Performance_Prediction

## Project Structure

```text
Student_Performance_Prediction/
│
├── app/
│   └── app.py
│
├── dataset/
│   └── student-mat.csv
│
├── model/
│   ├── student_performance_model.pkl
│   └── model_columns.pkl
│
├── notebook/
│   └── student_performance.ipynb
│
└── README.md
