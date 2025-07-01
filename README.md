# 🏦 Loan Default Prediction System

An advanced end-to-end machine learning system built with **PySpark**, **MLflow**, **Flask**, and **Streamlit**. This project predicts whether a customer is likely to default on a personal loan based on their financial and demographic data. It features a clean and interactive UI and is designed to be deployable on both local and cloud platforms like **AWS EC2**.

---

## 🚀 Key Features

- ✅ **PySpark-based ML pipeline** for scalable training
- ✅ **MLflow** model tracking and versioning
- ✅ **Flask API** for serving predictions
- ✅ **Streamlit UI** with clean UX and future insights
- ✅ **Modular & production-ready architecture**
- ✅ Ready for **cloud deployment on AWS**

---

## 📊 Input Features

- Age  
- Experience  
- Income  
- ZIP Code  
- Family Size  
- Credit Card Avg Spend  
- Education Level  
- Mortgage  
- Personal Loan (0/1)  
- Securities Account (0/1)  
- CD Account (0/1)  
- Online Banking (0/1)  
- Credit Card (0/1)

---

## 💡 Output

- **Prediction:** Whether a customer will default on a loan
- **Smart Insights:** Interactive visualizations and predictive financial insights

---

## 🧰 Tech Stack

| Layer           | Tools Used                   |
|----------------|-------------------------------|
| Data Processing| PySpark                       |
| ML Lifecycle   | MLflow                        |
| Backend API    | Flask                         |
| UI Dashboard   | Streamlit                     |
| Deployment     | Local & AWS EC2-ready         |

---

## 📦 Folder Structure

loan_default_project/
├── flask_api/
│ └── flask_app_py.py # Flask backend
├── spark_model/ # MLflow Spark models
├── streamlit_ui/
│ └── streamlit_app_py.py # Frontend UI
├── mlruns/ # MLflow tracking
├── data/ # (optional) sample dataset
├── pyspark_mlflow.py # Model training script
└── README.md

yaml
---

## 🛠 How to Run Locally

### 1. Train Model
```bash ```
python pyspark_mlflow.py
2. Launch Flask API
bash
python flask_api/flask_app_py.py
3. Start Streamlit UI
bash
streamlit run streamlit_ui/streamlit_app_py.py

📌 Author
Shaurya Chauhan
Data Science + Economics | ML Engineer Enthusiast
GitHub • LinkedIn
