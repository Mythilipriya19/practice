from pyspark.shell import spark
from pyspark.sql import SparkSession
from setuptools.command.alias import alias

spark= SparkSession.builder \
         .appName("name") \
         .getOrCreate()
sc=spark.sparkContext


data = [(1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "David"), (5, "Eve")]
columns = ["id", "name"]
df = spark.createDataFrame(data, columns)

repartitioned_df = df.repartition(3).show()

#coalesced_df = df.coalesce(1).show()

#res=df.select(df["name"].alias("fullname")).show()
