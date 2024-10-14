from pyspark.shell import spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from setuptools.command.alias import alias


spark= SparkSession.builder \
         .appName("name") \
         .getOrCreate()
sc=spark.sparkContext


data = [(1, "  Alice","laptop"), (2, "  Bob","phone"), (3, "Charlie","laptop"), (4, "David","botle"), (5, "Eve","cap")]
columns = ["id", "name","product"]
df = spark.createDataFrame(data, columns)



#res=df.withColumn("name",upper(df["name"])).show()
#res=df.withColumn('new_Name',trim(df['Name'])).show()
#res=df.withColumn('Name',substring(df['Name'],0,3)).show()
#res=df.withColumn('Name',translate(df['Name'],"a","x")).show()
#res=df.withColumn('Name',length(df['Name'])).show()
#res=df.withColumn('Name',lpad(df['Name'],8,'$')).show()
#res=df.withColumn('Name',repeat(df['Name'],n=2)).show()
#res=df.withColumn('Name',split(df['Name'],'a')).show()