# ************* Lesson 13  **************
# ************* Try Except **************
# Note: is used run a test on our program to test it against any run time error 
# we can specify the type of error every except handle
try:
    num1 = 10/0 
    num2 = int(input("Enter a number: "))
    print("the number is", num)
except ZeroDivisionError as err: 
    print(err)
except ValueError:
    print("Not a number!!")
