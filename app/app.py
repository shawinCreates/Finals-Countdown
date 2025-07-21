import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load('app/model.pkl')
scaler = joblib.load('app/minmaxscaler.pkl')

# Page configuration
st.set_page_config(
    page_title="Finals Countdown 🎓",
    page_icon="📘",
    layout="wide",
)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #1f4e79;'>🎓 Finals Countdown</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #555;'>Predict Your Score Before It Predicts Your Future</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- Layout Columns ---
col1, col2 = st.columns([2, 2])

with col1:
    st.subheader("🧮 Numerical Inputs")

    study_hours_per_day = st.slider("Study Hours per Day", 0.0, 10.0, 2.0)
    prep_days_before_exam = st.slider("Preparation Days Before Exam", 0, 60, 15)
    attendance_percentage = st.slider("Attendance Percentage (%)", 0, 100, 80)
    internal_marks = st.slider("Internal Marks (out of 50)", 0, 50, 30)
    internal_marks_weight = st.slider("Internal Marks Weight", 0.0, 1.0, 0.2)
    past_performance = st.slider("Past Performance (%)", 0, 100, 60)
    doubt_time = st.slider("Doubt Resolution Time (hours/week)", 0, 20, 2)

with col2:
    st.subheader("📋 Categorical Inputs")

    subject_difficulty = st.selectbox("Subject Difficulty", ["Easy", "Moderate", "Hard"])
    study_material_source = st.selectbox("Study Material Source", ["Textbooks", "YouTube", "Coaching", "Notes"])
    self_study_or_coaching = st.selectbox("Study Technique", ["Coaching", "Self-study", "Group-Study"])
    motivation_level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
    exam_anxiety_level = st.selectbox("Exam Anxiety Level", ["Low", "Medium", "High"])

# --- Mappings ---
motivation_dict = {"Low": 0, "Medium": 1, "High": 2}
anxiety_dict = {"Low": 0, "Medium": 1, "High": 2}
difficulty_dict = {"Easy": 0, "Moderate": 1, "Hard": 2}
study_dict = {"Textbooks": 2, "YouTube": 3, "Coaching": 0, "Notes": 1}
self_study_dict = {"Coaching": 0, "Self-study": 2, "Group-Study": 1}

# --- Prepare Data ---
input_dict = {
    'study_hours_per_day': study_hours_per_day,
    'prep_days_before_exam': prep_days_before_exam,
    'attendance_percentage': attendance_percentage,
    'internal_marks': internal_marks,
    'internal_marks_weight': internal_marks_weight,
    'subject_difficulty': difficulty_dict[subject_difficulty],
    'study_material_source': study_dict[study_material_source],
    'past_performance': past_performance,
    'self_study_or_coaching': self_study_dict[self_study_or_coaching],
    'motivation_level': motivation_dict[motivation_level],
    'doubt_resolution_time': doubt_time,
    'exam_anxiety_level': anxiety_dict[exam_anxiety_level]
}
input_df = pd.DataFrame([input_dict])
numerical_cols = ['study_hours_per_day', 'prep_days_before_exam', 'attendance_percentage',
                  'internal_marks', 'internal_marks_weight', 'past_performance', 'doubt_resolution_time']
input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

# --- Prediction ---
st.markdown("---")
center = st.columns([1, 2, 1])[1]

with center:
    st.subheader("📈 Final Marks Prediction")
    if st.button("🚀 Predict Final Exam Marks"):
        prediction = model.predict(input_df)[0]
        st.success(f"🎯 Your Predicted Marks: **{prediction:.2f} / 100**")
        st.progress(min(int(prediction), 100))

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Predictions powered by coffee, panic, and machine learning. ❤️ </p>", unsafe_allow_html=True)
