from pyspark.shell import spark

data=[('mythili',1),('priya',2),('anu',3)]
data2=[('mythili',1),('sri',2),('anu',4)]

schema=['name','id']
#schema2=['name','id']
j=spark.createDataFrame(data,schema)
j1=spark.createDataFrame(data2,schema)

#df=j.join(j1, on='id',how='inner')
#df=j.join(j1, on='id',how='right')
#df=j.join(j1, on='id',how='full')
# df=j.join(j1, on='id',how='leftanti')
#df=j.join(j1, on='id',how='leftsemi')
df=j.join(j1, 'id','left')
#df=j.crossJoin(j1)
df.show()