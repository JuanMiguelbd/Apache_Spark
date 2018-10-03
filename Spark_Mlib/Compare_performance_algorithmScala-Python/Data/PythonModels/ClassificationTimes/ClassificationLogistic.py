# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 15:19:50 2018

@author: Juan Miguel
"""

import time
from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression

if __name__ == "__main__":


    sparksession = SparkSession\
        .builder\
        .appName("Spark ML _LogisticRegression") \
        .config("spark.driver.memory", "8g") \
        .master("local[4]") \
        .getOrCreate()

    # Load data
    training = sparksession\
        .read\
        .format("libsvm")\
        .load("C:/datosmlib/MLlib/Classification_Data150000.400.txt")
        
    training.show()

    start_computing_time = time.time()


    lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

    # Fit the model
    lrModel = lr.fit(training)

    # Print the coefficients and intercept for logistic regression
    print("Coefficients: " + str(lrModel.coefficients))
    print("Intercept: " + str(lrModel.intercept))

    # We can also use the multinomial family for binary classification
    mlr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")

    # Fit the model
    mlrModel = mlr.fit(training)

    # Print the coefficients and intercepts for logistic regression with multinomial family
    print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
    print("Multinomial intercepts: " + str(mlrModel.interceptVector))
        
    total_computing_time = time.time() - start_computing_time
    print("Computing time: ", str(total_computing_time))

    
sparksession.stop()