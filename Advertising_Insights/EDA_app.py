import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

HTML_CSS_MARKDOWN = """
<style>
        .main-title {
            font-size : 38px;
            font-weight : 800;
            text-align : center;
            color : #4F8BF9;
            margin-bottom : 5px;
        }
        .subtitle {
            text-align : center;
            color : #9CA3AF;
            font-size : 16px;
            margin-bottom : 30px;
        }
        .section-title {
            font-size : 24px;
            font-weight : 700;
            color : #4F8BF9;
            padding-bottom : 8px;
            border-bottom : 2px solid #4F8BF9;
            margin-top : 20px;
            margin-bottom : 15px;
        }
        .info-card {
            background : linear-gradient(
                135deg , #172554 , #1E3A5F
            );
            padding : 20px;
            border-radius : 14px;
            border : 1px solid #334155;
            margin-bottom : 10px;
        }
        .card-label {
            color : #CBD5E1;
            font-size : 14px;
        }
        .card-value {
            color : #FFFFFF;
            font-size : 28px;
            font-weight : bold;
            margin-top : 8px;
        }
        div[data-testid = "stExpander"] {
            border-radius : 12px;
            border : 1px solid #334155;
        }
    </style>
"""
HTML_CSS_HEADER = """
    <div class="main-title">
        📊 Exploratory Data Analysis
    </div>

    <div class="subtitle">
        Discover patterns, understand your data, and uncover insights.
    </div>
"""
HTML_CSS_EX = """
    <style>
        div[data-testid = "stExpander"] {
            background-color : #172554;
            border : 1px solid #3B82F6;
            border-radius : 12px;
            overflow : hidden;
        }
        div[data-testid = "stExpander"] summary {
            background-color : #1E40AF;
            color : white;
        }
        div[data-testid = "stExpander"] details,
        div[data-testid = "stExpander"] div[data-testid ="stExpanderDetails"] {
            background-color : #172554;
            color : white;
        }
    </style>
"""
def hist_plot(df , x):
    fig = plt.figure()
    sns.histplot(data = df , x = x)
    st.pyplot(fig)

def scatter_plot(df , x , y , color):
    fig = plt.figure()
    sns.scatterplot(data = df , x = x , y = y , color = color)
    st.pyplot(fig)

def run_EDA_app():
    st.markdown(body = HTML_CSS_MARKDOWN , unsafe_allow_html = True)
    st.markdown(body = HTML_CSS_HEADER , unsafe_allow_html = True)
    df = pd.read_csv(filepath_or_buffer = "C:\\Users\\Lenovo\\Desktop\\Streamlit_Github\\Project_4\\Advertising.csv")
    subMenu = st.sidebar.selectbox(label = "EDA Menu" , options = ["Description" , "Visualization"])
    if subMenu == "Description":
        with st.expander("DataFrame"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html=True)
            st.header("DataFrame")
            st.dataframe(df)
        with st.expander("DataTypes"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html=True)
            st.header("DataTypes")
            st.dataframe(df.dtypes)
        with st.expander("Describe"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html=True)
            st.header("Describe")
            st.dataframe(df.describe().T)
    elif subMenu == "Visualization":
        with st.expander("Histogram"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html = True)
            st.header("Histogram")
            histMenu = st.selectbox(label = "Please Select Feature: " , options = ["None" , "TV" , "radio" , "newspaper" , "sales"])
            if histMenu == "TV":
                hist_plot(df , "TV")
            elif histMenu == "radio":
                hist_plot(df , "radio")
            elif histMenu == "newspaper":
                hist_plot(df , "newspaper")
            elif histMenu == "sales":
                hist_plot(df , "sales")
        with st.expander("Scatter Plot"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html = True)
            st.header("Scatter Plot")
            xMenu = st.selectbox(label = "Please Select X: " , options = ["TV" , "radio" , "newspaper"])
            yMenu = st.selectbox(label = "Please Select y: " , options = ["sales"])
            if xMenu == "TV" and yMenu == "sales":
                st.success("X : TV , Y : Sales")
                scatter_plot(df , x = "TV" , y = "sales" , color = "red")
            elif xMenu == "radio" and yMenu == "sales":
                st.success("X : Radio , Y : Sales")
                scatter_plot(df , x = "radio" , y = "sales" , color = "green")
            elif xMenu == "newspaper" and yMenu == "sales":
                st.success("X : Newspaper , Y : Sales")
                scatter_plot(df , x = "newspaper" , y = "sales" , color = "blue")
        with st.expander("Feature Correlation"):
            st.markdown(body = HTML_CSS_EX , unsafe_allow_html = True)
            st.success("Feature Correlation")
            fig = plt.figure()
            sns.heatmap(df.corr() , annot = True , cmap = "coolwarm" , fmt = ".2f")
            st.pyplot(fig)

