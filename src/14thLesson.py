# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : AttachmentTo14thLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
employee_file = open("src/AttachmentTo14thLesson.txt", "w")

if employee_file.readable():
    print(employee_file.read())
else:
    print("Not a readable file !!!")


employee_file.close()  # close the opened file
