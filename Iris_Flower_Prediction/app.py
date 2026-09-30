import streamlit as st
from EDA_app import run_EDA_app
from ML_app import run_ML_app

HTML_BANNER = """
    <div style="
       padding: 18px 22px;
       border-radius: 14px;
       background: #BEBDBF;
       border-left: 20px solid #9b5de5;
       margin-bottom: 25px;
    ">
       <h2 style="
           margin: 0;
           font-size: 28px;
           font-weight: 700;
           color: #212529
        ">
           🌸 Iris Flower Prediction
       </h2>
    </div>
"""


def main():
    Menu = ["Home" , "Exploratory Data Analysis" , "Machine Learning"]
    choice = st.sidebar.selectbox(label = "Menu" , options = Menu)
    if choice == "Home":
        st.markdown(HTML_BANNER , unsafe_allow_html = True)
        col1 , col2 = st.columns(spec = 2)
        with col1: 
            with st.expander("Exploratory Data Analysis" , expanded = True):
                st.info("Exploratory Data Analysis")
                st.markdown("""
                ### Understanding the Iris Dataset 🌸
                Explore the Iris dataset through statistical analysis
                and interactive visualizations. Discover patterns,
                compare flower measurements, and understand the
                differences between the three Iris species.
                """)
        with col2:
            with st.expander("Machine Learning" , expanded = True):
                st.info("Machine Learning")
                st.markdown("""
                ### Predicting Iris Flower Species 🤖
                Discover how Machine Learning can classify Iris
                flowers based on their physical measurements.
                Using a trained Support Vector Classifier (SVC),
                predict whether a flower belongs to Setosa,
                Versicolor, or Virginica.
                """)

    elif choice == "Exploratory Data Analysis":
        run_EDA_app()
    elif choice == "Machine Learning":
        run_ML_app()
if __name__ == "__main__":
    main()