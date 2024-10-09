from pyspark.shell import spark, sc
from pyspark.sql import session, SparkSession

# creating spark session:

# spark= SparkSession.builder \
#        .appName("name") \
#        .getOrCreate()

# creating spark context:

sc=spark.sparkContext
# creating RDD from local

# data=[1,2,3,4,5]
# rdd=spark.parallelize(data)
# print(rdd.collect())

# Read data from external source

# rdd=sc.textFile('employee3.csv')
# print(rdd.collect())

#Transformation:


# data=[1,2,3,4,5]

# rdd=sc.parallelize(data)
# result=rdd.map(lambda x:x**3)
# print(result.collect())


# rdd=sc.parallelize(data)
# result=rdd.filter(lambda x:x>3)
# print(result.collect())

# Union:
data=[1,2,3,4,5]
data2=[2,4,5,2]

rdd=sc.parallelize(data)
rdd2=sc.parallelize(data2)
result=rdd.union(rdd2)
print(result.collect())


