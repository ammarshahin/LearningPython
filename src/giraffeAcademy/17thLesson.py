# ************* Lesson 17  ****************
# *********** Classes & Objects **************

# We can import classes form other modules:
# from Student import Student   # from the module improt the class ( "*" to import all the file)
# from Student import *         # from the module improt ( "*" to import all the file)


# Or define in the same File:
class Student:  # define a class
    def __init__(self, name, major, gpa):  # initialization  Function (Constructor)
        self.name = name
        self.major = major
        self.gpa = gpa


s1 = Student("Jim", "Eng", 3.1)  # creating an object
print(s1.name)
print(s1.major)
print(s1.gpa)
