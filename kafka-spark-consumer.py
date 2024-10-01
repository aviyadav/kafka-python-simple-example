from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType,  IntegerType
from pyspark.sql.functions import from_json, col

# Init SparkSession
spark = SparkSession.builder\
    .appName("KafkaConsumer")\
    .getOrCreate()
        
# Read data from Kafka Topic
df = spark.readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers", "localhost:9092")\
    .option("subscribe", "quickstart-events")\
    .load()

# Convert Kafka value column from binary to string
kafka_df = df.selectExpr("CAST(value AS STRING)")

# Print the DataFrame to the console
query = kafka_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the streaming query to terminate
query.awaitTermination()

# Stop SparkSession
spark.stop()