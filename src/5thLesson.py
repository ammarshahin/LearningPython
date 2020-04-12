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
friends.extend(charArr)
print(friends)
