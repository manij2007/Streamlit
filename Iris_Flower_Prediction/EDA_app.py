import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib 
matplotlib.use(backend = "Agg")
import seaborn as sns
import plotly.express as px

HTML_BANNER_EDA = """
    <div style="
       padding: 18px 22px;
       border-radius: 14px;
       background: #BEBDBF;
       border-left: 20px solid #DBA507;
       margin-bottom: 25px;
    ">
       <h2 style="
           margin: 0;
           font-size: 28px;
           font-weight: 700;
           color: #212529
        ">
           Exploratory Data Analysis
       </h2>
    </div>
"""
def hist_plot(df , x):
    fig = plt.figure()
    sns.histplot(data = df , x = x)
    st.pyplot(fig)

def scatter_plot(df , x , y , hue = "species"):
    fig = plt.figure()
    sns.scatterplot(data = df , x = x , y = y , hue = hue)
    st.pyplot(fig)

def count_plot(df , x , hue = "species"):
    fig = plt.figure()
    sns.countplot(data = df , x = x , hue = hue)
    st.pyplot(fig)

def box_plot(df , x):
    fig = plt.figure()
    sns.boxplot(data = df , x = x)
    st.pyplot(fig)

def run_EDA_app():
    st.markdown(HTML_BANNER_EDA , unsafe_allow_html = True)
    df = pd.read_csv(filepath_or_buffer = "C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_2\\Iris.csv")
    subMenu = st.sidebar.selectbox(label = "EDA Menu" , options = ["Description" , "Visualization"])
    if subMenu == "Description":
        with st.expander("DataFrame"):
            st.info("DataFrame")
            st.dataframe(df)
        with st.expander("DataTypes"):
            st.info("DataTypes")
            st.dataframe(df.dtypes)
        with st.expander("Describe"):
            st.info("Describe")
            st.dataframe(df.describe().T)
    elif subMenu == "Visualization":
        with st.expander("Histogram"):
            st.info("Histogram")
            histMenu = st.selectbox(label = "Please Select Feature: " , key = "00" , options = ["None" , "sepal_length" , "sepal_width" , "petal_length" , "petal_width"])
            if histMenu == "sepal_length":
                st.success("Sepal Length")
                hist_plot(df , "sepal_length")
            elif histMenu == "sepal_width":
                st.success("Sepal Width")
                hist_plot(df , "sepal_width")
            elif histMenu == "petal_length":
                st.success("Petal Length")
                hist_plot(df , "petal_length")
            elif histMenu == "petal_width":
                st.success("Petal Width")
                hist_plot(df , "petal_width")
        with st.expander("Scatter Plot"):
            st.info("Scatter Plot")
            xMenu = st.selectbox(label = "Please Select X: " , options = ["sepal_length" , "sepal_width" , "petal_length" , "petal_width"])
            yMenu = st.selectbox(label = "Please Select y: " , options = ["sepal_width" , "sepal_length" , "petal_width" , "petal_length"])
            if xMenu == "sepal_length" and yMenu == "sepal_width":
                st.success("X : Sepal Length , Y : Sepal Width")
                scatter_plot(df , x = "sepal_length" , y = "sepal_width")
            elif xMenu == "sepal_width" and yMenu == "sepal_length":
                st.success("X : Sepal Width , Y : Sepal Length")
                scatter_plot(df , x = "sepal_width" , y = "sepal_length")
            elif xMenu == "petal_length" and yMenu == "petal_width":
                st.success("X : Petal Length , Y : Petal Width")
                scatter_plot(df , x = "petal_length" , y = "petal_width")
            elif xMenu == "petal_width" and yMenu == "petal_length":
                st.success("X : Petal Width , Y : Petal Length")
                scatter_plot(df , x = "petal_width" , y = "petal_length")
            elif xMenu == "sepal_width" and yMenu == "petal_width":
                st.success("X : Sepal Width , Y : Petal Width")
                scatter_plot(df , x = "sepal_width" , y = "petal_width")
            elif xMenu == "sepal_width" and yMenu == "petal_length":
                st.success("X : Sepal Width , Y : Petal Length")
                scatter_plot(df , x = "sepal_width" , y = "petal_length")
            elif xMenu == "sepal_length" and yMenu == "petal_width":
                st.success("X : Sepal Length , Y : Petal Width")
                scatter_plot(df , x = "sepal_length" , y = "petal_width")
            elif xMenu == "sepal_length" and yMenu == "petal_length":
                st.success("X : Sepal Length , Y : Petal Length")
                scatter_plot(df , x = "sepal_length" , y = "petal_length")
            elif xMenu == "petal_length" and yMenu == "sepal_width":
                st.success("X : Petal Length , Y : Sepal Width")
                scatter_plot(df , x = "petal_length" , y = "sepal_width")
            elif xMenu == "petal_length" and yMenu == "sepal_length":
                st.success("X : Petal Length , Y : Sepal Length")
                scatter_plot(df , x = "petal_length" , y = "sepal_length")
            elif xMenu == "petal_width" and yMenu == "sepal_width":
                st.success("X : Petal Width , Y : Sepal Width")
                scatter_plot(df , x = "petal_width" , y = "sepal_width")
            elif xMenu == "petal_width" and yMenu == "sepal_length":
                st.success("X : Petal Width , Y : Sepal Length")
                scatter_plot(df , x = "petal_width" , y = "sepal_length")
        with st.expander("Pie Plot"):
            st.info("Pie Plot")
            fig = px.pie(data_frame = df , names = "species")
            st.plotly_chart(fig , use_container_width = True)
        with st.expander("Count Plot"):
            st.info("Count Plot") 
            count_plot(df , x = "species")
        with st.expander("Box Plot"):
            st.info("Box Plot")
            boxMenu = st.selectbox(label = "Please Select Feature: " , key = "01" , options = ["None" , "sepal_length" , "sepal_width" , "petal_length" , "petal_width"])
            if boxMenu == "sepal_length":
                st.success("Sepal Length")
                box_plot(df , "sepal_length")
            elif boxMenu == "sepal_width":
                st.success("Sepal Width")
                box_plot(df , "sepal_width")
            elif boxMenu == "petal_length":
                st.success("Petal Length")
                box_plot(df , "petal_length")
            elif boxMenu == "petal_width":
                st.success("Petal Width")
                box_plot(df , "petal_width")
        with st.expander("Feature Correlation"):
            st.info("Feature Correlation")
            fig = plt.figure()
            sns.heatmap(pd.get_dummies(df , drop_first = False).corr() , annot = True , cmap = "coolwarm" , fmt = ".2f")
            st.pyplot(fig)
            
