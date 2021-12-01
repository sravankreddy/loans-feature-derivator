# loans-feature-derivator

Steps:

1. Install below docker components
     - Postgres db
     - kafka 
     - kafka connector
     - kafka schema registry
     - zookeaper
     - redis
     -s3 ninja (Aws s3 emulator if you dont have AWS account)
     
2. Used pycharm for development
3. Below is the deployment file for Postgres to support CDC 
4. Used postman to spin the debezium source connector, ( we can use curl command also), this connector will push data from postgres to kafka topics

    !![image](https://user-images.githubusercontent.com/6806807/144186625-f98141f0-a8d2-46fb-ac84-461068aabd14.png)
    
5. Kafka topics screenshot 
    !![image](https://user-images.githubusercontent.com/6806807/144187775-f8276c92-1c7f-4221-a2a9-783a14dba4da.png)
   
6. Develop the pyspark streaming code
7. Maintain all the configuration parameters in evn_properties.ini file. Configurations like brokers urls, schema registery url , redis/hbase url
8. I have downloaded couple of jars files which took huge amount of time to resolve jar dependency related errors, we can see them in lib directory
9. Stream the data from topic to AWS S3

Technologies Used :
1. Apache Spark (Pyspark , structured streaming)
2. Apache Kafka OR AWS Kinesis
3. Kafka Connectors
4. Kubernetes and Docker for kafka and Kafka connector 
5. Apache HBASE or REDIS or Gemfire
6. AWS EMR
7. TERRAFORM for cluster and solution deployment
8. AWS Sagemaker (optional)
9. AWS S3
10. Python

Used AWS S3 Emulator for testing and development and i can able to stream the data and loaded to s3 

! ![image](https://user-images.githubusercontent.com/6806807/144186152-90a81993-34c6-4c74-8655-335e3fa7e8f5.png)

Architecture:

!![image](https://user-images.githubusercontent.com/6806807/144185282-79088b86-1c10-4240-8564-1467f56c49a8.png)
