# Apache Spark RDD-Dataframe

In this section, i show some task about Apache Spark RDD - Dataframe.

## 1. Analisys_electricity.

The World Bank offers a large amount of open data. In this exercise we will focus on the % of population having access to electricity in all the countries of the world since 1960 to 2014.  The data can be obtained from this link: https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS. After selecting the CSV format you will get a zip file containing, among others, these two files:

API_EG.ELC.ACCS.ZS_DS2_en_csv_v2.csv
    
Metadata_Country_API_EG.ELC.ACCS.ZS_DS2_en_csv_v2.csv
After taking a look to the content of these files, write a program named electricityAnalysis.py that, given two years (e.g., 1970 and 1980), prints in the screen the average number of countries of each of the regions (South Asia, North America, etc.) having at least a 99% of electricity during all the years between two which have been indicated. The output must be ordered in descendent order by the percentage value, and it should look like this example (the data are invented): 

    Region                       Percentage

    -------------------           --------------

    North America                       100%

    Europe & Central Asia                99%


## 2. Clean_Data_Dataframe.

Typically, data to be analyzed in real world applications is not fully clean. Frequently, there are missing fields, invalid values, etc. 

A civil engineer is working in the design of a bridge, trying to find different alternatives, each of them having a total bridge weight and the degree of deformation in certain parts. After using an optimization software, she/he has obtained a .tsv file (attached to this task) with a number of rows indicating different trade-off designs. A plot of this file should look like like this graph:

Unfortunately, some lines/fields have invalid values (blank lines, missing values, characters instead of numbers, etc), and there are also repeteated lines.

This task consists in developing a Jupyter notebook with PySpark to read the file, remove all the invalid lines and remove those that are appears more than one time, and plot the clean data.


## 3. Comparing the running time of two equivalent solutions in PySpark.

This exercise is aimed at comparing the running time of two equivalent solutions in PySpark, one based on RDD and another on dataframe, to determine which is faster.

Given the dataset of the crimes of Chicago (https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2), write two programs crimeRDDAnalysis.py and crimeDataframeAnalysis.py that have to count the number of crimes per location and print the first 10 pairs (location,  count) ordered by count. 