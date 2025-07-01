# 🧠 Loan Default Prediction using PySpark
"""
This project demonstrates a complete PySpark-based machine learning pipeline for predicting loan default using structured data.
"""
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.feature import VectorAssembler
import mlflow
import mlflow.spark
import os

# Start Spark
spark = SparkSession.builder.appName("LoanDefaultPrediction").getOrCreate()

# Load data (replace with your actual dataset)
df = spark.read.csv("C:/Users/SHAURYA CHAUHAN/Desktop/DATA SCI/projects/loan_default_project/loan_data.csv", header=True, inferSchema=True)
