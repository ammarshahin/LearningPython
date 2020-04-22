class Student:  # define a class
    def __init__(self, name, major, gpa):  # initialization  Function (Constructor)
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    
