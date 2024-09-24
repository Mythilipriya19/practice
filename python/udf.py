# user define function
"""def add(fname,lname):
       print(fname,lname)

add("mythili","priya")"""

#adding
"""def add(a,b):
    c=a+b
    print(c)
add(20,40)"""

#Lambda Function:
"""x=lambda a,b: a-b
print(x(10,20))"""

#Return:
"""def add(a,b):
    c=a+b
    return c
add(20,40)

v=add(20,40)
print(v)"""

#Arbinory Function:
def add(*args):
    total=0
    for i in args:
        total += i
    return total


print(add(10,20,30))
