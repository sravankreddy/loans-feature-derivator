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

    def process_batch(self,df, epoch_id):
        r = redis.Redis(
            host='hostname',
            port= 6345,
            password='password')
        # get the client metrics
        # calculate the three metrics here
        # update the newly added metrics to redis feature store
        # continue streaming
        pass
