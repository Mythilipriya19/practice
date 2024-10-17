
from pyspark.sql.types import *
from pyspark.sql import SparkSession
spark= SparkSession.builder \
         .appName("name") \
         .getOrCreate()
sc=spark.sparkContext

#ARRAY:

# data=[('Sam',['Web'],()),('Ram',["DE","DS"]),('mythili',["De","maths"])]
# schema=StructType([
# StructField("name",StringType()),
# StructField("skill",StringType())
# ])

#Nested Array:

data=[('Sam',['Web'],(1,73026896)),('Ram',["DE","DS"],(2,98737609)),('mythili',["De","maths"],(2,2979787))]
schema=StructType([
StructField("name",StringType()),
StructField("skill",StringType()),
StructField("details", StructType([
    StructField('ID',IntegerType()),
    StructField('Number',IntegerType())
]))
])
df = spark.createDataFrame(data,schema)
df.show()






