# Narrow Transformation:
from pyspark.python.pyspark.shell import spark

sc=spark.sparkContext
# data=[1,2,3,4,5]

# rdd=sc.parallelize(data)
# result=rdd.map(lambda x:x**3)
# print(result.collect())


# rdd=sc.parallelize(data)
# result=rdd.filter(lambda x:x>3)
# print(result.collect())

# Union:
#data=[1,2,2,2,3,4,5]
# data2=[2,4,5,2]
#
# rdd=sc.parallelize(data)
# rdd2=sc.parallelize(data2)
# result=rdd.union(rdd2)
# print(result.collect())

# Distinct:
data = [1, 2, 2, 3, 4, 4]
rdd = sc.parallelize(data)

# Get distinct elements
result = rdd.distinct()

# Collect the results to display them
print(result.collect())  # Should output: [1, 2, 3, 4]




