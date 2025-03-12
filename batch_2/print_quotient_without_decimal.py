# Prompt user for two numbers and print the quotient without decimal places.
# If the second number is 0, print "Cannot divide by zero"

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

if num2 == 0:
    print("Cannot divide by zero.")
else:
    quotient = num1 // num2
    print("Quotient:", quotient)