# Using Lambda function
"""v=[1,2,3,4,5]
s=[2,3,4,1,2]
k=map(lambda x,y:x+y, s,v)
print(list(k))"""

#without lambda function
def string(n):
    return n*n
s=[2,4,5]
k=map(string,s)
print(list(k))

