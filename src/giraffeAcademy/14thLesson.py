
# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : src/AttachmentTo14thLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
# employee_file is an object the stores the file inside it
employee_file = open("text.txt", 'r')

if employee_file.readable():              # check if the file is readable or not
    # print(employee_file.read())         # read the entire file
    # print(employee_file.readline())     # read the first line  >> pops up the line in order
    # print(employee_file.readline())     # read the second line

    # read the all the lines and store them in a list
    employee_list = employee_file.readlines()  # making a list of lines
else:
    print("Not a readable file !!!")

for employee in employee_list:
    employee = str(employee)  # Convert the lines to string
    employee = employee.split(' - ') # splitting every line to individual elements
    print("Name = " + employee[0])
    print("Job = " + employee[1])
    print("ID = " + employee[2])
    print("\n")


employee_file.close()  # close the opened file

# Note: Every time we read a line from the file we move the curser to the next line !
