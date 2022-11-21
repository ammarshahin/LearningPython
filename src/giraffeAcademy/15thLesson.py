# ************* Lesson 15  **************
# *********** Writing to files **************
# Attach : text.txt

# open a the file and (r[read], w[writ], a[append], r+[read an write])
# "w" overwrites the entire file
# employee_file is an object the stores the file contents inside it
employee_file = open("text.txt", "a")

employee_file.write("Ahmed - HR - 64551315\n")
employee_file.write("Kelly - PR - 65416315\n")

employee_file.close()
