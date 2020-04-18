# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : AttachmentTo14thLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
employee_file = open("AttachmentTo14thLesson", "r")

if employee_file.readable():
    print(employee_file.read())
else:
    print("Not a readable file !!!")


employee_file.close()  # close the opened file
