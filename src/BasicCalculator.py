# ************* Basic Calculator Program **************

# convert the string entered from the user from string to float value
operand1 = float(input("Enter the first operand: "))
operation = input("Enter the operation needed: ")

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
    result = operand1

print("result = ", result)
