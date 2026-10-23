import streamlit as st
from EDA_app import run_EDA_app
from ML_app import run_ML_app

HTML_CSS_BANNER = """
    <style>
    .hero {
        background : linear-gradient(135deg , #101827 , #1e3a5f);
        padding : 35px 30px;
        border-radius : 18px;
        border : 1px solid #2c4564;
        margin-bottom : 25px;
        text-align : left;
    }
    .hero-tag {
        color : #65d5fa;
        font-size : 12px;
        font-weight : 700;
        letter-spacing : 3px;
        text-transform : uppercase;
    }
    .hero h1 {
        color : #ffffff;
        font-size : 42px;
        font-weight : 800;
        margin : 15px 0 12px 0;
        line-height : 1.2;
    }
    .hero p {
        color : #c1ccdc;
        font-size : 16px;
        line-height : 1.8;
        margin-bottom : 0;
    }
    .hero span {
        color : #65d5fa;
        font-weight : 600;
    }
    </style>
    <div class = "hero">
        <div class = "hero-tag">Marketing Analytics Dashboard</div>
        <h1>Advertising Insights 📊</h1>
        <p>
            Analyze advertising investments across
            <span>TV, Radio, and Newspaper</span>,
            visualize marketing trends, and discover
            how advertising impacts sales.
        </p>
    </div>
"""

HTML_CSS_BANNER_EX_HOME = """
<style>
    div[data-testid = "stExpander"] {
        background : linear-gradient(135deg , #111c2e , #172a43);
        border : 1px solid #2c4564;
        border-radius : 14px;
        margin-bottom : 15px;
        overflow : hidden;
    }
    div[data-testid = "stExpander"] summary {
        color : #65d5fa;
        font-size : 18px;
        font-weight : 700;
        padding : 12px;
    }
    div[data-testid = "stExpander"] details {
        border-radius : 14px;
    }
    .expander-content {
        color : #c1ccdc;
        font-size : 15px;
        line-height : 1.8;
        padding : 8px 5px;
    }
    .expander-content h4 {
        color : #65d5fa;
        font-size : 17px;
        margin-bottom : 8px;
    }
    .expander-content ul {
        padding-left : 22px;
    }
    </style>
"""

def main():
    Menu = ["Home" , "Exploratory Data Analysis" , "Machine Learning"]
    choice = st.sidebar.selectbox(label = "Menu" , options = Menu)
    if choice == "Home":
        st.markdown(body = HTML_CSS_BANNER , unsafe_allow_html = True)
        st.markdown(body = HTML_CSS_BANNER_EX_HOME , unsafe_allow_html = True)

        with st.expander("📊  Exploratory Data Analysis (EDA)"):
            st.markdown("""
            <div class = "expander-content">
            <h4>Discover Your Advertising Data</h4>

            Explore the Advertising dataset through interactive
            visualizations and statistical analysis.

            <ul>
                <li>Understand dataset structure and summary statistics.</li>
                <li>Analyze relationships between advertising channels and sales.</li>
                <li>Visualize distributions, correlations, and trends.</li>
                <li>Identify the most influential advertising channels.</li>
            </ul>
            </div>
            """ , unsafe_allow_html=True)

        with st.expander("🤖  Machine Learning — Polynomial Regression"):
            st.markdown("""
            <div class = "expander-content">

            <h4>Predict Sales with Polynomial Regression</h4>

            Build a machine learning model to explore nonlinear
            relationships between advertising expenditure and sales.
                        
            <ul>
                <li>Select advertising features for model training.</li>
                <li>Choose the polynomial degree.</li>
                <li>Train and evaluate the regression model.</li>
                <li>Compare actual and predicted sales.</li>
                <li>Explore model performance using R², MAE, and RMSE.</li>
            </ul>
            </div>
            """ , unsafe_allow_html=True)
    elif choice == "Exploratory Data Analysis":
        run_EDA_app()
    elif choice == "Machine Learning":
        run_ML_app()

if __name__ == "__main__":
    main()