

from pyspark.shell import spark
from pyspark.sql import Window
from pyspark.sql.functions import row_number,rank,dense_rank,lag
from pyspark.sql.functions import *



data=[('mythili','De',50000),('priya','hr',40000),('sri','IT',40000),('anu','De',60000),('anbu','IT',50000),('aruna','hr',45000),
      ('bob','IT',20000),('alice','De',20000),('sam','IT',40000)]
schema=['name','dept','sal']

df=spark.createDataFrame(data,schema)


window=Window.partitionBy('dept').orderBy('sal')
# df.withColumn('row_number',row_number().over(window)).\
# withColumn('rank',rank().over(window)).\
# withColumn('dense_rank',dense_rank().over(window)).\
df.withColumn('lag',lag('sal').over(window)).\
withColumn('lead',lead('sal').over(window)).show()

