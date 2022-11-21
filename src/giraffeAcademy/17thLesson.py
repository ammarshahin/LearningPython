
# ************* Lesson 17  ****************
# *********** Classes & Objects **************

# We can import classes form other modules:

# from the module "Student" import the class
# from student import Student

# from the module "student" import "*"  all
from student import *

s1 = Student("Jim", "Eng", 3.7)  # creating an object

print(s1.name)
print(s1.major)
print(s1.gpa)

if s1.on_honor_roll() == True:
    print("On honor roll!!")
