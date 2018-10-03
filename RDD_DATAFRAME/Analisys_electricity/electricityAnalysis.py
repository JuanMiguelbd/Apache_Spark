# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 18:14:28 2018

@author: Juan Miguel
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as func

def main() -> None:
          
    # I create a SparkSession.
    
    spark_session = SparkSession \
    .builder \
    .getOrCreate()
    
    logger = spark_session._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.WARN)
    
    
    # Now, We create the structure of the dataframe of electricity.  
    list_structType_elec = [StructField('CountryName', StringType(),False), \
                       StructField('CountryCode_elec', StringType(), False), \
                       StructField('IndicatorName', StringType(), False), \
                       StructField('IndicatorCode', StringType(), False)]

    for years in range(1960,2018):
        
        list_structType_elec.append(StructField("_" + str(years), DoubleType(),False))
    
    schema_elec = StructType(list_structType_elec)
       

    # We load the data of the dataFrame electricity.
    data_Frame_Electricity = spark_session\
                       .read\
                       .format("csv")\
                       .schema(schema_elec) \
                       .load("C:\DATOS\MASTER BIG DATA\Master Big Data\Modulo 9 ApacheSpark\py\Task\AdvancedTask1\API_EG.ELC.ACCS.ZS_DS2_en_csv_v2.csv")

    # We load the data of the dataFrame region.
    data_Frame_Region = spark_session\
                       .read\
                       .format("csv")\
                       .option("header", "True") \
                       .load("C:\DATOS\MASTER BIG DATA\Master Big Data\Modulo 9 ApacheSpark\py\Task\AdvancedTask1\Metadata_Country_API_EG.ELC.ACCS.ZS_DS2_en_csv_v2.csv")
    
    
    # Joins Dataframes Electricity with Region.
    dataframe_elec_region = data_Frame_Electricity.join(data_Frame_Region, \
                                                        data_Frame_Electricity.CountryCode_elec == data_Frame_Region["Country Code"])
        
    
    # Input Years init-end.    
    init_year = int(input("Introduce initial-Year Between 1960-2017: "))
    end_year = int(input("Introduce End-Year higher than " + str(init_year) + " and less than 2017: "))
    end_year= end_year+1
    
    
    # We filter all the countries whose 99% of population having access to electricity. For it, we create a variable called constritions and we use it to filter.
    # Afterthats we group it by regions.
    for year_number in range(init_year,end_year): 
        constritions ="_" + str(year_number) + " >= 99 AND "
    
    
    d_99_elec = dataframe_elec_region.filter(constritions).groupBy('Region').count().withColumnRenamed("count","Calculate_countries")
    #d_99_elec.show()
    
    # Now, We group all the countries by region.
    d_region = dataframe_elec_region.groupBy('Region').count().withColumnRenamed("count","Total_countries")
    #d_region.show()

    # we join dataframes region and elec_ above.
    d_final_region_percent = d_region.join(d_99_elec, 'Region')
    #d_final_region_percent.show()
    
    # Here, we calculate the percentage of countries whose 99% of population having access to electricity by regions.
    d_final_value_sort = d_final_region_percent.select(d_final_region_percent.Region, (100 * d_final_region_percent.Calculate_countries / d_final_region_percent.Total_countries) \
        .alias("Percentage")).sort("Percentage", ascending=False)
    #d_final_value_sort.show()
    
    # Lastly, we put pretty the result. 
    d_final_value =d_final_value_sort.select('Region',func.format_string("%2.0f%%", func.col('Percentage')).alias('Percentage'))
    
    d_final_value.show()
    
    # Stop spark_session
    spark_session.stop()
 
if __name__ == "__main__":
    
    main()