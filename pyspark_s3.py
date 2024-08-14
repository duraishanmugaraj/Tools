from pyspark.sql import SparkSession

# Initialize Spark session with S3 support
spark = SparkSession.builder \
    .appName("S3ReadExample") \
    .config("spark.hadoop.fs.s3a.credentials.provider", "com.amazonaws.auth.profile.ProfileCredentialsProvider") \
    .config("spark.hadoop.fs.s3a.access.key", "") \
    .config("spark.hadoop.fs.s3a.secret.key", "") \
    .config("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com") \
    .getOrCreate()
# Path to the CSV file in S3
s3_path = "s3a://ec2-spark-aws-files/creditcard.csv"

# Read the CSV file into a DataFrame
df = spark.read.csv(s3_path, header=True, inferSchema=True)
df.write \
    .format("csv") \
    .option("header", "true") \
    .save("s3a://ec2-spark-aws-files/creditcard_pyspark.csv")

# Show the DataFrame
df.show()
