# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:59:06 2018

@author: Juan Miguel
"""

from scipy import stats
import numpy as np
import pandas as pd


# We get the dataframe.
df = pd.read_excel('C:/datosmlib/MLlib/Task3_advanced/Time.xlsx', sheetname=1)

# Selecting the data. Time-Scala and Time-Python
scala=df['Time'][df['Programming_Language']=='Scala'] 
python=df['Time'][df['Programming_Language']=='Python'] 

# Implementing the Wilcoxon Test.
st, p_value = stats.wilcoxon(scala, python, zero_method='wilcox')  

# Print the results.
print(st,p_value)