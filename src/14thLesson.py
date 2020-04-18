# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : src/AttachmentTo14thLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
employee_file = open("src/AttachmentTo14thLesson.txt", "r") # employee_file is an object the stores the file inside it

if employee_file.readable():            # check if the file is readable or not 
    #print(employee_file.read())         # read the entire file 
    #print(employee_file.readline())     # read the first line
    #print(employee_file.readline())     # read the second line
    employee_list = employee_file.readlines()    # read the all the lines and store them in a list
else:
    print("Not a readable file !!!")

for line in employee_list:
    print(line)

employee_file.close()  # close the opened file

# Note: Every time we read a line from the file we move the curser to the next line !