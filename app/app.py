import streamlit as st
import joblib
import numpy as np
import pandas as pd
import random

# Load model and scaler
model = joblib.load('app/model.pkl')
scaler = joblib.load('app/minmaxscaler.pkl')

# Page configuration
st.set_page_config(
    page_title="Finals Countdown 🎓",
    page_icon="app/logo.png",
    layout="centered",
)
# Inject custom CSS
with open("app/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
with st.container():
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        st.image("app/logo.png", width=50)
    with col2:
        st.markdown("<h4 class='app-title'>Finals Countdown</h4>", unsafe_allow_html=True)

# Main Section: Title and Tagline
with st.container():
    st.markdown("""
    <div class='title-wrapper'>
        <h1 class='main-title' style='text-align: center; color: #1f4e79;'>🎓 Finals Countdown</h1>
        <h4 class='tagline' style='text-align: center;'>Predict Your Score Before It Predicts Your Future</h4>
    </div>
    """, unsafe_allow_html=True)


# --- Layout Columns ---
with st.container():
    col1, col2 = st.columns([2, 2])

    with col1:
        st.subheader("🎯 Your Study Stats")

        study_hours_per_day = st.slider("📘 How much do you *actually* study per day?", 0.0, 8.0, 2.0)
        prep_days_before_exam = st.slider("📅 When do you usually start exam prep?", 0, 45, 15)
        attendance_percentage = st.slider("🏫 Attendance (% because sometimes... life)", 0, 100, 80)
        internal_marks = st.slider("📝 Internal Marks (out of 100)", 0, 100, 30)
        internal_marks_weight = st.slider("⚖️ How much did you cheat?", 0.0, 1.0, 0.2)
        past_performance = st.slider("📊 Your Past Academic Vibes (%)", 0, 100, 60)
        doubt_time = st.slider("❓ Weekly Doubt Solving (hrs)", 0, 12, 2)

    with col2:
        st.subheader("😎 Study Personality")

        subject_difficulty = st.selectbox("📚 How scary is the subject?", [
            "🛌 Feels like a nap",
            "🙂 Manageable",
            "😵 Brain-twister",
            "😰 Panic-inducing",
            "💀 I’ve accepted my fate"
        ])

        study_material_source = st.selectbox("📖 Where do you get your knowledge drops from?", [
            "📚 Textbooks (old school)",
            "📺 YouTube (bless the creators)",
            "🏫 Coaching (parents’ choice)",
            "🗒️ Notes (copied 5 mins before test)"
        ])

        self_study_or_coaching = st.selectbox("👨‍🏫 Your Study Vibe", [
            "🏫 College (packaged learning)",
            "🧘 Self-study (solo grind)",
            "👨‍👩‍👧‍👦 Group Study (talk 90%, study 10%)"
        ])

        motivation_level = st.selectbox("🔥 Current Motivation Feels", [
            "😩 I don't feel like it",
            "🤷 I might... not sure",
            "😐 I’ll just prepare (maybe)",
            "😤 I *should* study",
            "💪 I will study *seriously*"
        ])

        exam_anxiety_level = st.selectbox("💥 Exam Anxiety Check", [
            "😭 I'm depressed (send help)",
            "😬 Nervous breakdown incoming",
            "😐 Meh, it's fine... maybe",
            "😎 Chill like a cucumber",
            "🧘 What’s an exam?"
        ])

# --- Vibe-Based Mappings ---
motivation_dict = {
    "😩 I don't feel like it": 1,
    "🤷 I might... not sure": 2,
    "😐 I’ll just prepare (maybe)": 3,
    "😤 I *should* study": 4,
    "💪 I will study *seriously*": 5
}

anxiety_dict = {
    "😭 I'm depressed (send help)": 5,
    "😬 Nervous breakdown incoming": 4,
    "😐 Meh, it's fine... maybe": 3,
    "😎 Chill like a cucumber": 2,
    "🧘 What’s an exam?": 1
}

difficulty_dict = {
    "🛌 Feels like a nap": 1,
    "🙂 Manageable": 2,
    "😵 Brain-twister": 3,
    "😰 Panic-inducing": 4,
    "💀 I’ve accepted my fate": 5
}

study_dict = {
    "📚 Textbooks (old school)": 2,
    "📺 YouTube (bless the creators)": 3,
    "🏫 Coaching (parents’ choice)": 0,
    "🗒️ Notes (copied 5 mins before test)": 1
}

self_study_dict = {
    "🏫 College (packaged learning)": 0,
    "🧘 Self-study (solo grind)": 2,
    "👨‍👩‍👧‍👦 Group Study (talk 90%, study 10%)": 1
}

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

        # 🎭 Fun titles based on prediction
        if prediction >= 90:
            title = "🧠 Undercover Genius"
            msg = "You're cruising to glory! Just don’t get too cocky 😎"
        elif prediction >= 75:
            title = "🚀 Exam Warrior"
            msg = "You're doing awesome! A little more push and you’re golden."
        elif prediction >= 60:
            title = "📚 Hustler-in-Progress"
            msg = "Solid effort! Stay consistent and the top is yours."
        elif prediction >= 40:
            title = "🔄 Midnight Crammer"
            msg = "You’ve got potential — time to fight distraction monsters!"
        else:
            title = "🛌 Dreamer"
            msg = "It’s okay. Maybe start by opening the book? Baby steps. 📖✨"

        # 🌟 Display character title
        st.markdown(f"### {title}")
        st.info(msg)

        # 🧃 Random fun tip (optional)
        tips = [
            "🔥 Pro Tip: Use Pomodoro — 25 min grind, 5 min meme scroll.",
            "😴 Don’t underestimate sleep. Brain = recharge battery.",
            "🎧 Study music helps. Try lo-fi, not death metal.",
            "📆 Make a plan. Even a bad one. Then improve it.",
            "💬 Talk about doubts — even your friend who scores 40 might know this one."
        ]
        st.caption(f"🧃 {random.choice(tips)}")


# --- Footer ---
st.markdown("<p style='text-align: center;'>Predictions powered by coffee, panic, and machine learning. ❤️ </p>", unsafe_allow_html=True)
st.markdown("<footer class='footer'> © 2025 Sabin Neupane. All rights reserved. </footer>", unsafe_allow_html=True)
