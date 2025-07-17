# 📋 Project Planning & Documentation

## 🎯 Project Title: **Finals Countdown**
> _Predict Your Score Before It Predicts Your Future_

---

## 🧩 1. Problem Statement

Many students study only in the final weeks or days before an exam. They often wonder whether their current effort will be enough to pass — or even score well. This project aims to build a machine learning model that predicts a student’s **final exam score** based on real-world inputs such as:

- Study time per day  
- Internal marks  
- Attendance  
- Study material used  
- Subject difficulty  
- Past academic performance

The goal is to provide:
- An accurate prediction of final exam performance
- Actionable feedback based on input features

---

## 🧠 2. Objectives

- 📌 Build a supervised regression model to predict final exam scores.
- 📌 Deploy an interactive web application to take student inputs and return predictions.
- 📌 Provide interpretability using SHAP to show which factors most influence the prediction.
- 📌 Make the app fun, accessible, and useful for last-minute learners.

---

## 🛠️ 3. Tools & Technologies

| Category       | Tools Used                            |
|----------------|----------------------------------------|
| **Language**   | Python 3.11                            |
| **Libraries**  | pandas, scikit-learn, XGBoost, SHAP    |
| **App UI**     | Streamlit / Flask                      |
| **Deployment** | Streamlit Cloud, Render, or Railway    |
| **Versioning** | Git + GitHub                           |
| **Testing**    | pytest or unittest                     |

---

## 🧪 4. ML Workflow

1. **Data Collection**  
   - Create synthetic or real student performance data

2. **Data Preprocessing**  
   - Handle missing values, encode categories, scale features

3. **Exploratory Data Analysis**  
   - Visualize distributions, correlations, patterns

4. **Model Building**  
   - Train/test split  
   - Models: Linear Regression, Random Forest, XGBoost  
   - Evaluation: MAE, RMSE, R²

5. **Interpretability**  
   - Use SHAP to explain model predictions

6. **Web App Development**  
   - Build a form-based UI for predictions  
   - Display output and visualizations

7. **Deployment**  
   - Deploy app on Streamlit Cloud or Render  
   - Enable live demo access for users and recruiters

---

## 🧰 5. Feature List

- [x] Student input form (study hours, attendance, etc.)
- [x] Prediction output (final exam score)
- [ ] SHAP-based explanation of prediction
- [ ] Score improvement suggestions
- [ ] Dashboard for educators (optional bonus)

---

## 📌 6. Potential Extensions (Future Work)

- Add a recommendation engine (how to improve score)
- Track user inputs over time and show progress
- Add classification (Pass/Fail) mode
- Expand dataset for real-world deployment in schools

---

## 💬 7. Credits & Acknowledgements

- Built by Sabin Neupane (shawinCreates).  
- Inspired by the panic of exams and the power of ML 😅  
- Predictions powered by coffee, panic, and machine learning.

---
