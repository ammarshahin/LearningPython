# ************* Lesson 18  ****************
# *********** Class Function **************

from Student import Student  # import the class Student from the Student Module

# create a list of all the students and input their info
students = [Student("Ahmed", "Accounting", 3.1),
            Student("Mohammed", "Enginnering", 3.5),
            Student("Kim", "PHD", 2.5),
            Student("Jim", "Science", 3.2),
            Student("Karl", "Philosophy", 3),
            Student("Harry", "Physics", 4.5)]

# Loop throw the whole list and and cheek for gba
for student in students:
    if student.on_honor_roll():
        print(student.name, "How study", student.major,
              "is a cleaver student with", student.gpa)
    else:
        print(student.name, "How study", student.major,
              "is a good student with", student.gpa)
