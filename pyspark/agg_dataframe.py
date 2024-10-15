from pyspark.shell import spark

from pyspark.sql.functions import *

data=[('mythili',1.5),('priya',2),('anu',3)]


schema=['name','age']

df=spark.createDataFrame(data,schema)


#res=df.groupBy("name").agg(sum('age')).show() ---agg using groupby
# res=df.agg(max('age')).show()   ---max value
# res=df.agg(min('age')).show()   ---min value
# res=df.agg(avg('age')).show()   --avg value
res=df.select('age',round(df['age'])).alias('Result')
res.show()
# res=df.agg(first('age')).show()  ---first,last
# res=df.agg(count_distinct('name')).show()  ---count_distinct