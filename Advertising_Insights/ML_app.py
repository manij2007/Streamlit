import streamlit as st
import joblib
import numpy as np
import pandas as pd

def run_ML_app(): 
    st.set_page_config(page_title = "Sales Prediction" , page_icon = "📊" , layout = "centered")
    poly = joblib.load("C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_4\\poly.pkl")
    scaler = joblib.load("C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_4\\scaler.pkl")
    model = joblib.load("C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_4\\model.pkl")
    st.title("📊 Sales Prediction App")
    st.subheader("Advertising Budget")
    st.write("Predict sales using advertising budgets.")
    with st.form("prediction_form"):
        tv = st.number_input(label = "TV" , min_value = 1.0 , max_value = 296.0 , value = 100.0 , format = "%.0f" , step = 5.0)
        radio = st.number_input(label = "radio" , min_value = 0.0 , max_value = 49.0 , value = 20.0 , format = "%.0f" , step = 5.0)
        newspaper = st.number_input(label = "newspaper" , min_value = 1.0 , max_value = 114.0 , value = 50.0 , format = "%.0f" , step = 5.0)
        submitted = st.form_submit_button("Predict Sales" , type = "primary")
        
    if submitted:
        X = pd.DataFrame(data = [[tv , radio , newspaper]] , columns = ["TV" , "radio" , "newspaper"])
        X_poly = poly.transform(X)
        X_scaled = scaler.transform(X_poly)
        prediction = model.predict(X_scaled)[0]

        st.success("Prediction completed")
        st.balloons()
        st.metric("Predicted Sales : " , f"{prediction : .1f}")
