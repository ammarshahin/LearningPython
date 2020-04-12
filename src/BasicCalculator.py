# ************* Basic Calculator Program **************

#******************* factorial function ****************
def factorial(num):
    return num

# convert the string entered from the user from string to float value
operand1 = float(input("Enter the first operand: "))
operation = input("Enter the operation needed ex(+,-,*,/): ")

if operation == "+":
    operand2 = float(input("Enter the second operand: "))
    result = operand1 + operand2
elif operation == "-":
    operand2 = float(input("Enter the second operand: "))
    result = operand1 - operand2
elif operation == "*":
    operand2 = float(input("Enter the second operand: "))
    result = operand1 * operand2
elif operation == "/":
    operand2 = float(input("Enter the second operand: "))
    result = operand1 / operand2
elif operation == "^":
    operand2 = float(input("Enter the second operand: "))
    result = pow(operand1, operand2)
elif operation == "!":
    result = factorial(operand1)
else:
    result = none
    pass

print("result =", result)
