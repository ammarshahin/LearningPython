# ************* Lesson 7 **************
# ************* Functions **************

# Note: Any function has an indent(Tab before any line of code inside the function)
# Ex:
# create a function
''' 
def say_hi():
    print("inside")
    print("inside")
    print("inside")
    print("inside")
print("outside")
'''
'''
def say_hi(name, age):
    print("hello " + name + " you are " + age)

say_hi("ammar", "25")
say_hi("Mike", "20")
'''


def cube(num):
    return num*num*num


print(cube(3))
print(cube(4))
