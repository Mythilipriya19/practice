try:
    a=int(input("enter name:"))
except Exception as e:
    print(e)
else:
    print(" all ok")
finally:
    print("hy helo")

