#single inheritence
"""class grandfather:
    def parent(self):
        print("always good")
class child(grandfather):
        pass
obj=grandfather()
obj.parent()"""
#multiple inheritence
"""class parent:
    def method(self):
        print("hi")
class parent1:
    def method1(self):
        print("hello")
class child(parent,parent1):
    def method2(self):
        print("hey")
obj=child()
obj.method()
obj.method1()"""
#multi level inheritence
"""class parent1:
    def method(self):
        print("hello")
class parent2:
    def method1(self):
        print("hey")
class child(parent1, parent2):
    def method2(self):
        print("okkkkkkkkk")
obj=child()
obj.method1()
obj.method2()"""
#hierarchical inheritence
"""class parent:
    def method_parent(self):
        print("hello")
class child1(parent):
    def method_child1(self):
        print("hey")
class child2(parent):
    def method_child2(self):
        print("okkkkkkkkk")
obj1=child1()
obj2=child2()

obj1.method_parent()
obj1.method_child1()
obj2.method_parent()
obj2.method_child2()"""
#hybrid inheritence
"""class grandfather:
    def method(self):
        print("hello")
class parent(grandfather):
    def method1(self):
        print("hey")
class parent1(grandfather):
    def method2(self):
        print("okkkkkkkkk")
class child(parent, parent1):
    def method3(self):
        print("hii")
obj=child()
obj.method()
obj.method1()
obj.method2()
obj.method3()"""

