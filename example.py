from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("PySpark Example with Sleep") \
    .getOrCreate()

# Sample data
data = [
    ("Alice", 34),
    ("Bob", 45),
    ("Cathy", 29),
]

# Create a DataFrame
df = spark.createDataFrame(data, ["Name", "Age"])

# Perform a simple transformation
df_transformed = df.withColumn("AgePlusOne", col("Age") + 1)

# Show the DataFrame
df_transformed.show()

# Sleep for 10 minutes (600 seconds)
print("Sleeping for 10 minutes...")
time.sleep(600)

# Continue with additional processing if needed
print("Woke up from sleep!")

# Stop the SparkSession
spark.stop()
