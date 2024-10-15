from pyspark.python.pyspark.shell import spark

data=[(1,'mythili'),(2,'aruna'),(3,'anu')]
schema=['id','name']

df=spark.createDataFrame(data,schema)
#res=df.filter((df['id']>3)&(df['name']=='David')).show() ----AND

#res=df.filter((df['id']>3)|(df['name']=='David')).show() ----OR