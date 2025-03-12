# Prompt user for two numbers and print the quotient with 2 decimal places.
# If the second number is 0, print "Cannot divide by zero"

n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))

if n2 == 0:
    print("Cannot divide by zero.")
else:
    result = round(n1/n2, 2)
    print("Quotient:", result)