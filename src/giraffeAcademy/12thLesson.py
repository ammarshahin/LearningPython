# ************* Lesson 12 **************
# ***** 2D Lists and Nested loops ******

number_grid = [  # 2D list
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

'''
print(number_grid[0][2]) # access the element
'''

for row in number_grid:  # row is now a list of columns
    for col in row:
        print(col)
