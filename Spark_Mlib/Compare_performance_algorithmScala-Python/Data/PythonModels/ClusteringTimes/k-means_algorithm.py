# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:07:14 2018

@author: Juan Miguel
"""

import time
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession

if __name__ == "__main__":


    sparksession = SparkSession\
        .builder\
        .appName("Spark ML _KMeans") \
        .config("spark.driver.memory", "8g") \
        .master("local[4]") \
        .getOrCreate()

    # Load data
    dataset = sparksession\
        .read\
        .format("libsvm")\
        .load("C:/datosmlib/MLlib/Clustering_Data150000.300.txt")
        
    dataset.show()

    start_computing_time = time.time()

  # Prepare training and test data.
    train, test = dataset.randomSplit([0.7, 0.3], seed=42)

    # Trains a BisectingKMeans model.

    kmeans = KMeans().setK(2).setSeed(1)
    model_kmeans = kmeans.fit(dataset)

    # Make predictions with bestModel parameters
    predictions_kmeans = model_kmeans.transform(test)
    predictions_kmeans.show(10)

    # Evaluate clustering Model.
    cost = model_kmeans.computeCost(test)
    print("Within Set Sum of Squared Errors = " + str(cost))

    # Shows the result.
    centers_kmeans = model_kmeans.clusterCenters()
    print("Cluster Centers: ")
    for center in centers_kmeans:
        print(center)
        
    total_computing_time = time.time() - start_computing_time
    print("Computing time: ", str(total_computing_time))

    
sparksession.stop()

