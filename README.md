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