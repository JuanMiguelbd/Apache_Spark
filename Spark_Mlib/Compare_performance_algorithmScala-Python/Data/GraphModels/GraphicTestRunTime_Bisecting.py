# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:09:45 2018

@author: Juan Miguel
"""

import matplotlib.pyplot as plt


resultTimeScala = [53,39,30,26]
resultTimePython = [70,43,34,28]
cores =["1","2","3","4"]
plt.plot(cores,resultTimeScala,label="Scala")
plt.plot(cores,resultTimePython,label="Python")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel('Time (sg.)')
plt.xlabel('Number of cores')
plt.suptitle('Execution Time Test Scala-Python Kmeans')
plt.grid()
plt.show()
