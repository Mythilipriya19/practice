from py4j.protocol import STRING_TYPE

from pyspark.python.pyspark.shell import spark

from pyspark.sql.types import StructType, StructField, IntegerType, StringType



data = [('mythili', 1), ('aruna', 2)]

# datatype define

schema = StructType([

    StructField('Name', StringType()),

    StructField('Age', IntegerType())

])

df = spark.createDataFrame(data=data, schema=schema)

# using dictionary

data=[{'id':1,'name':'mythili'},
      {'id':2,'name':'aruna'}]

df.show()

df.printSchema()
