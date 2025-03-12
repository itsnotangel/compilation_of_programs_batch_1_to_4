#  Prompts the user for two numbers and prints the bigger number. 

num1 = float(input("Enter Number 1: ")) 
num2 = float(input("Enter Number 2: "))

if num1 > num2:
    print(num1, "is the bigger number.")
elif num1 < num2:
    print(num2, "is the bigger number.")
else:
    print("The numbers are equal.")