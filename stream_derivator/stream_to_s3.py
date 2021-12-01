from pyspark.sql import SparkSession
import os
from pyspark.sql.avro.functions import from_avro, to_avro
from pyspark.sql import functions as f
import requests
from config import  _app_config as config
from stream_derivator import feature_generator as features
import logging

log = logging.getLogger('stream_to_s3')

def stream_to_s3(topic, checkpoint_dir, data_directory, schemaregistry, brokers):
    # retrieve the latest schema
    spark = config.AppConfig.get_spark_session()
    response = requests.get('{}/subjects/{}-value/versions/latest/schema'.format(schemaregistry, topic))
    schema_value = response.text
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", brokers) \
        .option("subscribe", topic) \
        .option("startingOffsets", "earliest") \
        .option("mode", "DROPMALFORMED") \
        .load()
    op = {}
    op["mode"] = "PERMISSIVE"
    flatten_df = df \
        .selectExpr("substring(value, 6) as avro_value") \
        .select(from_avro(f.col("avro_value"), schema_value, op).alias("loans"))\
        .select("loans.after.*")

    flatten_df.writeStream\
       .format("csv")\
       .option("path",data_directory)\
       .outputMode("append") \
       .foreachBatch(features.feature_generator) \
       .option("checkpointLocation", checkpoint_dir) \
       .start()\
       .awaitTermination()

