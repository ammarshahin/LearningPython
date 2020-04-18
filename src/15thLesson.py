# ************* Lesson 14  **************
# *********** Reading files **************
# Attach : src/AttachmentToFilesLesson.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
# employee_file is an object the stores the file contents inside it
employee_file = open("src/AttachmentToFilesLesson.txt", "a")

employee_file.write("Ahmed - HR - 64551315")

employee_file.close()
