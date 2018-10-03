import time
import sys
from pyspark import SparkConf, SparkContext
 
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark-submit wordcount <file>", file=sys.stderr)
        exit(-1)
    
    # SparkContext represents the connection to a Spark cluster.
    spark_conf = SparkConf().setMaster('local[1]')
    spark_context = SparkContext(conf=spark_conf)
    
    logger = spark_context._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.WARN)
    
    # Start computing time.
    start_computing_time = time.time()

    # I create a RRD where I do several transformations of the data, and lastly execute an action to get a result.

    output = spark_context \
        .textFile(sys.argv[1]) \
        .map(lambda line: line.split(',')) \
        .filter(lambda w: w[7] != 'Location Description')  \
        .map(lambda w: (w[7],1)) \
        .reduceByKey(lambda a, b: a + b) \
        .sortBy(ascending=False, keyfunc=lambda x: x[1]) \
        .collect()
    
    # Stop computing time        
    total_computing_time = time.time() - start_computing_time
           
    
    
    # Printing the results.
    print('Number of crimes per location: ', '\n')    
    
    for (word, count) in output:
        print("%s -> %s" % (word,count))
    
    print("Computing time: ", total_computing_time)
    print(output[1][0],output[2][0])
    
    # Stopping spark_Context
    spark_context.stop()


# Chart bar about Number of crimes per location.

#y_pos = np.arange(len(output))
y_pos = np.arange(15)
objects = [output[num][0] for num in range(15)]
performance = [output[num][1] for num in range(15)]
plt.barh(y_pos, performance, align='center', color='orange', alpha=0.8)
plt.yticks(y_pos, objects)
plt.xlabel('Numbers')
plt.title('Number of crimes per location')
 
plt.show()