# Prompt user to input two numbers and print all the numbers between the numbers entered.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

if num1 == num2:
    print("Equal numbers.")
elif num1 + 1 == num2 or num2 + 1 == num1:
    print("Consecutive numbers.")
else:
    start = min(num1, num2)
    end = max(num1, num2)

    for num in range(start + 1, end):
        print(num)