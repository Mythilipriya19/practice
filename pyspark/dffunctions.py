from pyspark.shell import spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import when
from setuptools.command.alias import alias


spark= SparkSession.builder \
         .appName("name") \
         .getOrCreate()
sc=spark.sparkContext


data = [(1, "Alice","laptop"), (2, "Bob","phone"), (3, "Charlie","laptop"), (4, "David","botle"), (5, "Eve","cap")]
columns = ["id", "name","product"]
df = spark.createDataFrame(data, columns)

# Dataframe Functions:

#res=df.select("name").show()    --select
#res=df.filter(df["id"]>1).show()  --Filter
#res=df.where(df["id"]<3).show()   --Where
#res=df.filter(df["name"].like("%e")).show() --LIKE

#res=df.withColumn('Salary',when(df["id"]==1,"1000").otherwise("2000")).show() ---When & Otherwise
#res=df.describe().show() ----describe()
#res=df.groupBy("product").sum("id").orderBy("product",desc).show()