# Prompt user to enter 10 numbers. Subtract the sum of the 9 numbers from the first number entered. 

num1 = float(input("Enter Number 1: "))
total = num1

for count in range(9):
    number = float(input("Enter Number " + str(count+2) + ": "))
    total -= number

print("Total after subtracting the next nine numbers' sum from the first:", total)