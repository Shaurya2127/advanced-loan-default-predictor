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
# ✅ Drop the ID column
df = df.drop("ID")
print("Columns in your DataFrame:", df.columns)

# Preprocessing (example)
feature_cols = [col for col in df.columns if col != 'loan_default']
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
rf = RandomForestClassifier(labelCol="Personal Loan", featuresCol="features")

pipeline = Pipeline(stages=[assembler, rf])

# Train/test split
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# Train the model ✅
model = pipeline.fit(train_df)

# Save model to local path
model_save_path = "spark_model"
model.write().overwrite().save(model_save_path)

# Log model to MLflow
with mlflow.start_run():
    mlflow.spark.log_model(spark_model=model, artifact_path="pyspark-model")

print("✅ Model trained, saved, and logged to MLflow.")
