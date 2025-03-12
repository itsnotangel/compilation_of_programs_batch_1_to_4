# Prompt user to enter two numbers and print the remainder of the two numbers.

num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    remainder = num1 % num2
    print("Remainder:", remainder)