


from pyspark.shell import spark


# Read single file:

df=spark.read.format('csv').option("header",value='True').load('employee3.csv')
df.show()

# df=spark.read.csv(path='employee3.csv',header=True)
# df.show()

# Read multiple files:

   # df=spark.read.csv(path=['employee3.csv','employee3.csv'])

#read all csv files:
#inside the path we don't need enter that particular file link instead of folder link

    #df=spark.read.csv(path='')

