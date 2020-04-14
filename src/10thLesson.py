# ************* Lesson 10 **************
# ************* Loops *************

########################## while loop #################################
# ex:
# while <Condition>:
#   loop code
#   loop code
#   loop code
#   loop code
# Not loop code
'''
i = 1
while i <= 10:
    print(i)
    i += 1
'''

########################## for Loop #################################
# ex:
# for <index> in <Array>:
#   loop code
#   loop code
#   loop code
#   loop code
# Not loop code
'''
# this loop is looping through the string
for letter in "Giraffe Academy":
    print(letter)
'''
'''
# this loop is looping through the Array
num_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for every_element in num_array:
    print(every_element)
'''
'''
# this loop will loop throughout the Array of strings
friends = ["Chandler", "Rachel", "Monica", "Ross", "Phebe", "Joy"]
for friend in friends:
    print("We Love you", friend)
'''

# this loop will loop through a range of numbers
for num in range(1,10):
    print(num)
