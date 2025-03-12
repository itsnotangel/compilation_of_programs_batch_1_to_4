# Prompt user to enter 10 numbers and display all unique numbers. 
# For numbers with duplicate, display only the first entry.

num_list = []
duplicates = []
for count in range(10):
    num = float(input("Enter number " + str(count + 1) + ": "))
    if num not in duplicates:
        num_list.append(num)
        duplicates.append(num)

print(num_list)
    
