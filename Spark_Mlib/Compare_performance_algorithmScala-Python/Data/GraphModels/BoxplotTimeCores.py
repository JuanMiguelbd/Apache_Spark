# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:09:45 2018

@author: Juan Miguel
"""

import sys as os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

df = pd.read_excel('C:/datosmlib/MLlib/Task3_advanced/Time.xlsx', sheetname=1)

print(df.head())

sns.set(style="ticks")

sns.boxplot(x="Cores", y="Time", hue="Programming_Language", data=df, palette="PRGn")
sns.despine(offset=10, trim=True)
   



