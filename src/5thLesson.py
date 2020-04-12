# ************* Lesson 5 **************
# ************* Lists(Arrays) **************

# Note: Python index the array from the start to the end && and from end to start as well but with {-} sign
# BackEnd Indexing:
#           -4   |  -3   |   -2   |   -1
friends = ["Kev", "Karen", "Ahmed", "Jim"]  # array of strings
boolArr = [True, False, False, True]  # array of boolens

print(friends[1])   # karen
print(friends[-3])  # karen as well (BackEnd Indexing)
print(friends[1:3])  # the elements from 1 to 3
print(friends[1:])  # the elements from 1 to the end
print(friends[:2])  # the elements from the start to the element index 2
