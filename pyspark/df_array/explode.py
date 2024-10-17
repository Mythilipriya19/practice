from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import explode, explode_outer

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"])
]

df = spark.createDataFrame(data, ["id", "fruits"])
# res = df.withColumn('fruitss', explode('fruits'))   ---Explode
#res = df.withColumn('fruitss', explode_outer('fruits'))  ---Explode_outer
res.show(truncate=False)