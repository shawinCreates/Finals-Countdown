import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('app/model.pkl')
scaler = joblib.load('app/minmaxscaler.pkl')

# App title
st.title("🎓 Finals Countdown: Final Exam Marks Predictor")
st.write("This app predicts students' final exam marks based on study habits and internal performance.")

# Input fields
study_hours_per_day = st.slider("Study Hours per Day", 0.0, 10.0, 2.0)
prep_days_before_exam = st.slider("Preparation Days Before Exam", 0, 60, 15)
attendance_percentage = st.slider("Attendance Percentage", 0, 100, 80)
internal_marks = st.slider("Internal Marks", 0, 50, 30)
internal_marks_weight = st.slider("Internal Marks Weight", 0.0, 1.0, 0.2)
past_performance = st.slider("Past Performance", 0, 100, 60)
doubt_time = st.slider("Doubt Resolution Time (hours/week)", 0, 20, 2)

motivation_level = st.selectbox("Motivation Level", ["Low", "Medium", "High"])
exam_anxiety_level = st.selectbox("Anxiety Level", ["Low", "Medium", "High"])
subject_difficulty = st.selectbox("Subject Difficulty", ["Easy", "Moderate", "Hard"])
study_material_source = st.selectbox("Study Material Source", ["Textbooks", "YouTube", "Coaching", "Notes"])
self_study_or_coaching = st.selectbox("Study Techniques", ["Coaching", "Self-study", "Group-Study"])

# Encoding categorical inputs (same as training)
motivation_dict = {"Low": 0, "Medium": 1, "High": 2}
anxiety_dict = {"Low": 0, "Medium": 1, "High": 2}
difficulty_dict = {"Easy": 0, "Moderate": 1, "Hard": 2}
study_dict = {"Textbooks": 2,"YouTube": 3, "Coaching": 0, "Notes": 1}
self_study_dict = {"Coaching": 0, "Self-study": 2, "Group-Study": 1}

# Prepare input for prediction
features = np.array([[study_hours_per_day, prep_days_before_exam, attendance_percentage, internal_marks, internal_marks_weight,
                     difficulty_dict[subject_difficulty], study_dict[study_material_source ], past_performance,self_study_dict[self_study_or_coaching], 
                      motivation_dict[motivation_level],doubt_time, anxiety_dict[exam_anxiety_level]
                       ]])

features = scaler.transform(features)
# Predict
if st.button("Predict Final Exam Marks"):
    prediction = model.predict(features)[0]
    st.success(f"🎯 Predicted Final Exam Marks: **{prediction:.2f} / 100**")
