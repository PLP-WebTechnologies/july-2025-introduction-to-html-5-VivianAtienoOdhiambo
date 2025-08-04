# a simple calculator module
#ask the user for the first number
try:
    num1 = float(input("Enter first number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
    #ask the user for the second number
try:
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()
    #ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")
# perform the operation and print the result
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num1 / num2
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
    exit()

print("Result:", result)