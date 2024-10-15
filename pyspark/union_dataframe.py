from pyspark.shell import spark

data=[('mythili',1),('priya',2),('anu',3)]
data2=[(1,'mythili'),(2,'sri'),(3,'kalai')]

schema=['name','id']
schema2=['id','name']
rdd1=spark.createDataFrame(data,schema)
rdd2=spark.createDataFrame(data2,schema2)

# df=rdd1.unionByName(rdd2)   --UnionByName
#df=rdd1.union(rdd2)          --Union
df=rdd1.unionAll(rdd2)
df.show()