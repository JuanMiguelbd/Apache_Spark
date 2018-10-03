# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:11:51 2018

@author: Juan Miguel
"""

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
import time

spark_conf = SparkConf().setMaster('local[3]')
spark_context= SparkContext(conf=spark_conf)

def main() -> None:

    # Start computing time.
    start_computing_time = time.time()

    # Get or Create SparkSession.
    spark_session = SparkSession.builder \
          .appName("Based on Dataframe") \
          .getOrCreate()
    
    # We load the data from CSV file.
    dataframeCrime = spark_session.read.csv(path='Crimes_-_2001_to_present.csv',
                        sep=',',
                        encoding='UTF-8',
                        comment=None,
                        header=True,
                        inferSchema=True)

    # Stop computing time        
    total_computing_time = time.time() - start_computing_time

    #dataframeCrime.show(n=5, truncate=False)
    #dataframeCrime.select('Location Description').show()
    
    # Getting results and printing.
    dataframeCrime.groupBy('Location Description') \
        .count() \
        .sort('count',ascending=False) \
        .show()
    
    print('\n',"Computing time: ", total_computing_time)

    # Stopping sparkContext.
    spark_context.stop()


if __name__ == "__main__":
    
    main()