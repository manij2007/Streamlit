# 🌸 Iris Flower Prediction

An interactive **Machine Learning web application** built with **Streamlit** to explore the Iris dataset and predict flower species based on their physical measurements.

The application combines Exploratory Data Analysis (EDA), interactive data visualizations, and a trained Support Vector Classifier (SVC) model in a simple and user-friendly interface.

## ✨ Features

### 📊 Exploratory Data Analysis (EDA)

* Explore the Iris dataset and its statistical summaries.
* Inspect DataFrame contents and data types.
* Visualize feature distributions using histograms.
* Analyze relationships between flower measurements with scatter plots.
* Explore species distribution using pie and count plots.
* Examine feature distributions using box plots.
* Investigate feature correlations with a heatmap.

### 🤖 Machine Learning Prediction

* Predict Iris flower species using a pre-trained **Support Vector Classifier (SVC)**.
* Input four flower measurements:

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width
* Classify flowers into three species:

  * Setosa
  * Versicolor
  * Virginica
* Display predictions through an interactive interface.

### 🎨 Interactive Web Interface

* Built with Streamlit.
* Organized navigation through a sidebar menu.
* Custom HTML banners and expandable sections.
* Interactive charts and measurement inputs.

## 🛠️ Technologies Used

* **Python** — Core programming language
* **Streamlit** — Web application framework
* **Pandas & NumPy** — Data manipulation and numerical operations
* **Matplotlib & Seaborn** — Data visualization
* **Plotly Express** — Interactive charts
* **Joblib** — Loading the trained model
* **Scikit-learn** — Machine Learning model

## 📁 Project Structure

```text
Iris-Flower-Prediction/
│
├── app.py
├── EDA_app.py
├── ML_app.py
├── Iris.csv
├── svc_model.pkl
└── README.md
```

## ⚙️ Installation & Usage

**1. Clone the repository**

```bash
git clone <repository-url>
cd Iris-Flower-Prediction
```

**2. Install the required dependencies**

```bash
pip install streamlit pandas numpy matplotlib seaborn plotly scikit-learn joblib
```

**3. Run the application**

```bash
streamlit run app.py
```

Make sure `Iris.csv` and `svc_model.pkl` are available at the paths expected by the application. Update the file paths in the Python scripts if necessary.

## 🎯 Project Objective

This project demonstrates how **Machine Learning and Exploratory Data Analysis can be integrated into an interactive web application**. It provides practical experience with data visualization, model deployment, user input handling, and multi-page-style navigation using Streamlit.

