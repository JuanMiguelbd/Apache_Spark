# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:09:45 2018

@author: Juan Miguel
"""

import matplotlib.pyplot as plt


resultTimeRDD = [149,117,117,111]
resultTimeDataframe = [26,14,10,8]
cores =["1","2","3","4"]
plt.plot(cores,resultTimeRDD,label="RDD")
plt.plot(cores,resultTimeDataframe,label="Dataframe")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel('Time (sg.)')
plt.xlabel('Number of cores')
plt.suptitle('Comparasion Execution Time Test RDD-Dataframe')
plt.grid()
plt.show()
