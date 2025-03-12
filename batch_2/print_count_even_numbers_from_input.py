# Prompt user to enter ten numbers and print the number of even numbers from the input.

even_count = 0

for count in range(10):
    number = int(input("Enter number " + str(count+1) + ": "))
    if number % 2 == 0:
        even_count += 1

print("Number of even numbers:", even_count)