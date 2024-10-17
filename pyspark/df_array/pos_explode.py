from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import explode, explode_outer,posexplode,posexplode_outer

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"]),
    (4,None)
]

df = spark.createDataFrame(data, ["id", "fruits"])


#res = df.select('id', posexplode('fruits').alias('pos','fruits'))  ----posexplode


#res=df.select('id',posexplode_outer('fruits').alias('one','two'))  ----posexplode_outer
res.show(truncate=False)