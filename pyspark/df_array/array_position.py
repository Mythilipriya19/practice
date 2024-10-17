from pyspark.python.pyspark.shell import spark
from pyspark.sql.functions import *

data = [
    (1, ["apple", "banana", "orange"]),
    (2, ["grape", "mango", "apple"]),
    (3, ["strawberry", "kiwi"])
]

df = spark.createDataFrame(data, ["id", "fruits"])
df1=df.withColumn('result',array_position('fruits','apple')).show(truncate=False)

