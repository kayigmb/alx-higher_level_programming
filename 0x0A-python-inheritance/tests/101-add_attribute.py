##!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))!/usr/bin/python3
MyInt = __import__("100-my_int").MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
