from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pwmgr_dataset import main

if __name__ == "__main__":
    conf = SparkConf().setAppName('pwmgr_dataset')
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)

    main.etl_job(sc, sqlContext)
