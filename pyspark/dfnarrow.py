from pyspark.shell import spark
from pyspark.sql import SparkSession

spark= SparkSession.builder \
         .appName("name") \
         .getOrCreate()
sc=spark.sparkContext
data=[(1, "Alice"), (2, "Bob"), (3, "Charlie"),(1,"Alice")]
rdd=sc.parallelize(data)

# df.select("name","id").show()  ---SELECT
#df.filter(df.id > 1).show()     ---FILTER
from pyspark.sql.functions import col, aggregate

#nc=df.withColumn("age",col("id")+20).show() ----Add newcolumn
#rn=df.withColumnRenamed("name","fullname").show() ---rename

#d=df.drop("id").show() ---delete column
#agg=df.groupBy("name").count().show()  ---aggregate()
#s=df.sort(df.name.desc()).show()   ---sorting

#l=df.limit(1).show()    ---limit
#d=df.distinct().show()    ---remove duplicates
#s=df.orderBy(df.name.desc()).show() --orderby