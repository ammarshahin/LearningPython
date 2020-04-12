# ************* Lesson 5 **************
# ************* Lists(Arrays) **************

# Note: Python index the array from the start to the end && and from end to start as well but with {-} sign
# BackEnd Indexing:
#           -4   |  -3   |   -2   |   -1
friends = ["Kev", "Karen", "Ahmed", "Jim"]  # array of strings
boolArr = [True, False, False, True]  # array of boolens
charArr = ["A", "B", "C", "D"]

print(friends[1])   # karen
print(friends[-3])  # karen as well (BackEnd Indexing)

# the elements from 1 to 2 {up to 3 but not including the 3rd element} >> ["B" , "C"]
print(charArr[1:3])
# the elements from 1 to the end {up to the end and including the last element} >> ["B" , "C" , "D"]
print(charArr[1:])
# the elements from the start to the element index 2 {up to 2 but not including the 2 element} >> ["A" , "B"]
print(charArr[:2])
