import streamlit as st
import numpy as np
import joblib

HTML_BANNER_ML = """
    <div style="
       padding: 18px 22px;
       border-radius: 14px;
       background: #BEBDBF;
       border-left: 20px solid #0D6986;
       margin-bottom: 25px;
    ">
       <h2 style="
           margin: 0;
           font-size: 28px;
           font-weight: 700;
           color: #212529
        ">
           Machine Learning
       </h2>
    </div>
"""

def run_ML_app():
    st.markdown(HTML_BANNER_ML , unsafe_allow_html = True)

    with open("C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_2\\svc_model.pkl", "rb") as file:
        model = joblib.load(file)

    st.title("🌸 Iris Flower Prediction")
    st.divider()

    sepal_length = st.number_input("Sepal Length (cm)" , min_value = 4.3 , max_value = 7.9 , value = 5.0 , step = 0.1 , format = "%.1f") 
    sepal_width = st.number_input("Sepal Width (cm)" , min_value = 2.0 , max_value = 4.4 , value = 3.0 , step = 0.1 , format="%.1f")
    petal_length = st.number_input("Petal Length (cm)" , min_value = 1.0 , max_value = 6.9 , value = 3.5 , step = 0.1 , format="%.1f")
    petal_width = st.number_input("Petal Width (cm)" , min_value = 0.1 , max_value = 2.5 , step = 0.1 , format="%.1f")

    if st.button("Predict Species" , type = "primary"):
        input_data = np.array([[sepal_length , sepal_width , petal_length , petal_width]])

        prediction = model.predict(input_data)[0]

        species = {0 : "Setosa" , 1 : "Versicolor" , 2 : "Virginica"}

        predicted_species = species.get(prediction , str(prediction))
        
        st.success(f"Predicted Species : {predicted_species}")

        st.balloons()
