import pyspark.sql.functions as f
from pyspark.sql import SparkSession
from config import _app_config
import logging
import pyspark.sql.dataframe as dfs
import redis

log = logging.getLogger('feature_generator')
class feature_generator:
    _spark_session: SparkSession = None
    app_config: _app_config = None

    def __init__(self, spark_session: SparkSession, app_config: app_config):
        self._spark_session = spark_session
        self.app_config = app_config

   # This method is in progress
    def process_batch(self,df, epoch_id):
        r = redis.Redis(
            host='hostname',
            port= 6345,
            password='password')
        '''
        Approach:  
         1. client.paid_loans.count - number of previously paid loans for this client.
              Key is Client_id and value is number of previously paid amounts 
         2. client.days_since_last_late_payment.count : Counts number of days sinse last payment done 
              Key will be client_id and  value will be last late payment in redis
        Pull above values for given client_id and update in redis feature store 
        '''
        pass
