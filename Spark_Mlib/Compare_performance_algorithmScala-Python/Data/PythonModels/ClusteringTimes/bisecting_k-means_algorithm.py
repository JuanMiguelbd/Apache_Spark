# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:07:14 2018

@author: Juan Miguel
"""

import time
from pyspark.ml.clustering import BisectingKMeans
from pyspark.sql import SparkSession

if __name__ == "__main__":


    sparksession = SparkSession\
        .builder\
        .appName("Spark ML Bisecting_KMeans") \
        .config("spark.driver.memory", "8g") \
        .master("local[1]") \
        .getOrCreate()

    # Load data
    dataset = sparksession\
        .read\
        .format("libsvm")\
        .load("C:/datosmlib/MLlib/Clustering_Data100000.200.txt")
        
    dataset.show()

    start_computing_time = time.time()

    # Prepare training and test data.
    train, test = dataset.randomSplit([0.7, 0.3], seed=42)

    # Trains a BisectingKMeans model.

    bkm = BisectingKMeans().setK(2).setSeed(1)
    model_bkm = bkm.fit(dataset)

    # Make predictions with bestModel parameters
    predictions_bkm = model_bkm.transform(test)
    predictions_bkm.show(10)

    # Evaluate clustering Model.
    cost = model_bkm.computeCost(test)
    print("Within Set Sum of Squared Errors = " + str(cost))

    # Shows the result.
    centers_bkm = model_bkm.clusterCenters()
    print("Cluster Centers: ")
    for center in centers_bkm:
        print(center)

 
    total_computing_time = time.time() - start_computing_time
    print("Computing time: ", str(total_computing_time))

    
sparksession.stop()

