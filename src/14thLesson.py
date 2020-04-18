# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : src/AttachmentTo14thLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
# employee_file is an object the stores the file inside it
employee_file = open("src/AttachmentTo14thLesson.txt", "r")

if employee_file.readable():            # check if the file is readable or not 
    print(employee_file.read())         # read the entire file 
    print(employee_file.readline())     # read the first line
    print(employee_file.readline())     # read the second line
    print(employee_file.readlines())    # read the all the lines and store them in a list
else:
    print("Not a readable file !!!")

employee_file.close()  # close the opened file
