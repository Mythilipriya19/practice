from functools import reduce
v=[12,2,2,3,2]
k=reduce(lambda x,y:x*y, v)
print(k)