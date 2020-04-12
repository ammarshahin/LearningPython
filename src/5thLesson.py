# ************* Lesson 5 **************
# ************* Lists(Arrays) **************

# Note: Python index the array from the start to the end && and from end to start as well but with {-} sign
# BackEnd Indexing:
#           -4   |  -3   |   -2   |   -1
friends = ["Kev", "Karen", "Ahmed", "Jim"]  # array of strings
print(friends[1])   # karen
print(friends[-3])  # karen as well (BackEnd Indexing)

friends[1] = "Mike"  # change the value of the list elements
print(friends[1])   # Mike


# ******************** list ranges *****************************
charArr = ["A", "B", "C", "D"]

# the elements from 1 to 2 {up to 3 but not including the 3rd element} >> ["B" , "C"]
print(charArr[1:3])
# the elements from 1 to the end {up to the end and including the last element} >> ["B" , "C" , "D"]
print(charArr[1:])
# the elements from the start to the element index 2 {up to 2 but not including the 2 element} >> ["A" , "B"]
print(charArr[:2])


# ******************** list functions *****************************

# Append whole list at the end of the main one
friends.extend(charArr)
print(friends)

# Append element at the end of the main list
friends.append("Mohammed")
print(friends)

# Insert element at any location in the main list
friends.insert(2, "Mahmoud")
print(friends)

# remove element from the main list
friends.remove("A")
friends.remove("B")
friends.remove("C")
friends.remove("D")
print(friends)

# get the last element of the list and remove it
temp = friends.pop()
print(temp)
print(friends)

# get the index of the element in the list
temp = friends.index("Ahmed")
print("Ahmed is at : " + str(temp))

# get the count of a specific element in the list
friends.append("Mohammed")
friends.append("Mohammed")
friends.append("Mohammed")
print(friends)
print("Mohammed has been repeated " + str(friends.count("Mohammed")) + " times")

friends.remove("Mohammed")
friends.remove("Mohammed")
friends.remove("Mohammed")
print(friends)

# clear the entire elements from the main list
friends.clear()
print(friends)
