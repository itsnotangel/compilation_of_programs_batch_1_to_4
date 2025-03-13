# Prompt user to enter ten numbers and print the number of odd numbers.

number_of_odd = 0

for count in range(10):
    number = int(input("Enter number " + str(count + 1) + ": "))
    if number % 2 != 0:
        number_of_odd += 1

print("Number of odd numbers:", number_of_odd)