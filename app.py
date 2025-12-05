import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("best_model.pkl")

st.title("Student Exam score Predictor")

Study_Hours = st.slider("Study Hour Per Day",0.0,12.0,1.0)
Attendance = st.slider ("Attendace in class" , 0.0 , 100.0 , 50.0)
Mental_Health = st.slider ("Mental Health Rate(1-10)",1.0,10.0,1.0)
Sleep_Hours = st.slider("Sleep Hours per Night ", 0.0 , 12.0 , 6.0)
Part_Time_Job = st.selectbox("Part Time Job ",["No","Yes"])

ptj_encoder = 1 if Part_Time_Job == "Yes" else 0

if st.button("Predict Exam Score"):
    input_data = np.array([[Study_Hours,Attendance,Mental_Health,Sleep_Hours,ptj_encoder]])
    prediction = model.predict(input_data)[0]

    prediction = max(0,min(100,prediction))
    
    st.success(f"Predicted Exam Score : {prediction}")