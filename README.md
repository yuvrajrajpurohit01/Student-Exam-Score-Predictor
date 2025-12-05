# Student Exam Score Predictor

A concise machine learning project that predicts a student's final exam score based on lifestyle and study-related factors such as study hours, Attendance , sleep duration, mental health , and daily habits. This project includes a complete end-to-end ML workflow along with an interactive Streamlit web app. 

---

## Project Overview
This project builds a regression model that learns patterns from students Habit data and predicts exam performance. It demonstrates practical machine learning concepts including EDA, preprocessing, model training, hyperparameter tuning, and deployment.

---

## Project Structure

### **Dataset**
- **`student_habits_performance.csv`**
  - Contains all input features and the target score value used for model training.

### **Input Features**
- **Study Hours per Day** — Average time spent studying.
- **Attendance (%)** — Overall class attendance.
- **Mental Health Rating (1–10)** — Self-reported mental wellness score.
- **Sleep Hours per Night** — Average sleep duration.
- **Part-Time Job (Yes/No)** — Whether the student works while studying.

### **Notebook**
- **`notebook.ipynb`**
  - Includes the complete workflow:
    - Data loading, cleaning, and preprocessing with Pandas  
    - Exploratory Data Analysis (EDA) using Matplotlib/Seaborn  
    - Feature engineering  
    - Training multiple regression models (Linear Regression, Random Forest, Decision Tree)  
    - Model evaluation + hyperparameter tuning  
    - Exporting the final model as a `best_model.pkl` file using Joblib  

### **Deployment**
- **`app.py`**
  - A Streamlit-based web application  
  - Loads the trained `best_model.pkl` model  
  - Accepts user inputs  
  - Generates real-time exam score predictions  

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-Learn  
- Matplotlib, Seaborn  
- Streamlit  
- Joblib  

<img width="1594" height="923" alt="Screenshot 2025-12-05 152224" src="https://github.com/user-attachments/assets/5224b9de-c80f-46dd-8722-944df74221d1" />

