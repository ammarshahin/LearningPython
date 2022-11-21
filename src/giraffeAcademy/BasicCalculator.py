
# ************* Basic Calculator Program **************
# ******************* Factorial function ****************
def factorial(num):
    if num > 0:
        return factorial(num - 1) * num

    return 1


def calc():

    try:
        operand1 = float(input("1st operand: "))
        operation = input("Enter the operation needed ex(+,-,*,/,^,!): ")
    except ValueError:
        print("invalid Input")
        return

    if operation == "+":
        operand2 = float(input("2nd  operand: "))
        result = operand1 + operand2
    elif operation == "-":
        operand2 = float(input("2nd  operand: "))
        result = operand1 - operand2
    elif operation == "*":
        operand2 = float(input("2nd  operand: "))
        result = operand1 * operand2
    elif operation == "/":
        operand2 = float(input("2nd  operand: "))
        try:
            result = operand1 / operand2
        except ZeroDivisionError as err:  # save the error message in a string variable "err"
            print(err)
            result = False
    elif operation == "^":
        operand2 = float(input("2nd  operand: "))
        result = pow(operand1, operand2)
    elif operation == "!":
        result = int(factorial(operand1))
    else:
        result = False

    if result == False:
        print("invalid Input")
    else:
        print("result =", result)


calc()

#! notes : "pass" >> is used to The pass statement is used as a placeholder for future code.
#! When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
#! Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
