# Prompt user to enter 10 numbers and display all unique numbers. 
# For numbers with duplicate, display only the first entry.

num_list = []

for count in range(10):
    num = float(input("Enter number " + str(count + 1) + ": "))
    if num not in num_list:
        num_list.append(num)

print("The numbers are:", num_list)