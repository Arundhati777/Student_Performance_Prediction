import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("model/student_performance_model.pkl")
model_columns = joblib.load("model/model_columns.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("🎓 Student Performance Prediction")
st.write(
    "Enter the student's academic information to predict "
    "their final grade (G3)."
)

st.divider()

# -----------------------------
# Student Information
# -----------------------------
st.subheader("📚 Student Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=15,
        max_value=25,
        value=17
    )

    studytime = st.number_input(
        "Study Time",
        min_value=1,
        max_value=4,
        value=2
    )

    failures = st.number_input(
        "Past Failures",
        min_value=0,
        max_value=4,
        value=0
    )

with col2:
    absences = st.number_input(
        "Absences",
        min_value=0,
        max_value=100,
        value=5
    )

    G1 = st.number_input(
        "First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

    G2 = st.number_input(
        "Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Final Grade", use_container_width=True):

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model_columns
    )

    input_data.loc[0, "age"] = age
    input_data.loc[0, "studytime"] = studytime
    input_data.loc[0, "failures"] = failures
    input_data.loc[0, "absences"] = absences
    input_data.loc[0, "G1"] = G1
    input_data.loc[0, "G2"] = G2

    prediction = model.predict(input_data)[0]

    st.success(
        f"🎯 Predicted Final Grade (G3): **{prediction:.2f} / 20**"
    )

    if prediction >= 15:
        st.info("Excellent predicted performance! 🌟")
    elif prediction >= 10:
        st.info("Good predicted performance. 👍")
    else:
        st.warning("The student may need additional academic support. 📖")