# 📊 Advertising Insights Dashboard

An interactive **Streamlit dashboard** for exploring advertising data and understanding how marketing investments across TV, radio, and newspaper relate to sales. The application combines Exploratory Data Analysis (EDA) with a Machine Learning section built around **Polynomial Regression**.

## ✨ Features

### 🏠 Home Dashboard
- Custom HTML/CSS hero banner and styled information panels.
- Simple sidebar navigation between Home, Exploratory Data Analysis, and Machine Learning.

### 🔎 Exploratory Data Analysis (EDA)
- Preview the dataset and inspect column data types.
- Review descriptive statistics.
- Explore feature distributions with interactive histogram selection.
- Visualize advertising expenditure versus sales using scatter plots.
- Examine feature relationships with a correlation heatmap.

### 🤖 Machine Learning
- Train a Polynomial Regression model to explore nonlinear relationships between advertising expenditure and sales.
- Select input features and polynomial degree.
- Compare actual and predicted sales.
- Evaluate model performance using **R², MAE, and RMSE**.

## 🧰 Tech Stack

- **Python**
- **Streamlit** — interactive web application.
- **Pandas** — data loading and analysis.
- **Matplotlib & Seaborn** — data visualization.
- **Scikit-learn** — machine learning and model evaluation.
- **HTML & CSS** — custom interface styling.

## 📁 Project Structure

```text
.
├── app.py
├── EDA_app.py
├── ML_app.py
├── Advertising.csv
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bat
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit pandas matplotlib seaborn scikit-learn
```

### 4. Prepare the Dataset

Place `Advertising.csv` in the project directory and ensure the application loads it using the correct file path.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the dashboard.

## 📈 Dataset

The project uses an advertising dataset containing **TV**, **radio**, and **newspaper** advertising expenditure, alongside **sales**. These features are used to explore marketing patterns and build a regression model for sales prediction.

## 💡 Project Goal

Transform advertising data into meaningful insights through interactive visualizations, statistical
