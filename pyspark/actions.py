from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext

#collect
data=[1,2,3,4,5]

rdd=sc.parallelize(data)
#print(rdd.count())
#print(rdd.first())
#print(rdd.take(2))
#print(rdd.top(2))
res=rdd.reduce(lambda x,y:x+y)
print(res)



