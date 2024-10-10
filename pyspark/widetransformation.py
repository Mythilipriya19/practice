from pyspark.python.pyspark.shell import spark

from practice.pyspark.RDD import result, data2

sc=spark.sparkContext

# GroupByKey:


#
# rdd_group=rdd.groupByKey()
# result = rdd_group.collect()
#
# for key , value in result:
#      print(key , list(value))

#ReaduceByKey:

# rdd_group=rdd.reduceByKey(lambda x,y:x+y)
# result = rdd_group.collect()
# print(result)

#Joins:

data1=[(1,'Rex'),(2,'Sam'),(3,"Babu")]

data2=[(1,'Salem'),(2,'erode'),(3,"Thirupur")]

rdd1=sc.parallelize(data1)
rdd2=sc.parallelize(data2)

res=rdd1.join(rdd2)

print(res.collect())