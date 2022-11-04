# ************* Lesson 13  **************
# ************* Try Except **************
# Note: is used run a test on our program to test it against any run time error
# we can specify the type of error every except handle
try:
    num2 = int(input("Enter a number: "))
    num1 = 10 / num2
    print("the number is", num1)
except ZeroDivisionError as err:  # here we saved the error message in a variable err
    print(err)
except ValueError:
    print("Not a number!!")
