import logging
from pyspark.sql import SparkSession
import os
import findspark
findspark.init("E:\myworks\spark\spark-3.2.0-bin-hadoop3.2\spark-3.2.0-bin-hadoop3.2")

log = logging.getLogger('App_Config')

class AppConfig:

    @staticmethod
    def get_spark_session():
        os.environ['JAVA_HOME'] = "C:\Program Files\OpenJDK\jdk-8.0.262.10-hotspot"
        os.environ[
            'PYSPARK_SUBMIT_ARGS'] = '--jars spark-sql-kafka-0-10_2.12-3.2.0.jar,spark-streaming-kafka-0-10-assembly_2.12-3.2.0.jar,spark-avro_2.12-3.2.0.jar,commons-pool2-2.11.1.jar,hadoop-aws-3.2.0.jar,aws-java-sdk-bundle-1.11.563.jar pyspark-shell'
        spark = SparkSession \
            .builder \
            .master("local") \
            .appName("Python Spark SQL basic example") \
            .getOrCreate()
        spark.sql("select 1 as id ").show()
        spark.sql("set spark.sql.streaming.forceDeleteTempCheckpointLocation = true")
        spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.aws.credentials.provider",
                                                          "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider")
        spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIAIOSFODNN7EXAMPLE")
        spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key",
                                                          "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")
        spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "http://localhost:9444/s3/")

        return spark

