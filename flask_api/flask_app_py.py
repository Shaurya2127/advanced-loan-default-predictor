from pyspark.ml import PipelineModel
from flask import Flask, request, jsonify
import json
from pyspark.sql import SparkSession
import pandas as pd

# Start Spark
spark = SparkSession.builder.appName("LoanDefaultAPI").getOrCreate()

# Correct path: model saved manually earlier
model = PipelineModel.load("spark_model")  # ✅

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Ensure it's a list of one record to support DataFrame input
    if isinstance(data, dict):
        data = [data]

    df = pd.DataFrame(data)

    # ✅ Drop any column not used in the model
    allowed_columns = [
        "Age", "Experience", "Income", "ZIP Code", "Family",
        "CCAvg", "Education", "Mortgage", "Personal Loan",
        "Securities Account", "CD Account", "Online", "CreditCard"
    ]
    df = df[[col for col in df.columns if col in allowed_columns]]

    spark_df = spark.createDataFrame(df)
    prediction = model.transform(spark_df)
    result = prediction.select("prediction").collect()[0][0]
    return jsonify({"prediction": int(result)})

if __name__ == "__main__":
    app.run(debug=True)
