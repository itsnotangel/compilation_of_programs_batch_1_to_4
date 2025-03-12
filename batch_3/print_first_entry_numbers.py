# Prompt user to enter 10 numbers and display all unique numbers. 
# For numbers with duplicate, display only the first entry.

num_list = []
seen_num = []

for count in range(10):
    num = float(input("Enter number " + str(count + 1) + ": "))
    if num not in seen_num:
        num_list.append(num)
        seen_num.append(num)

print("The numbers are:", num_list)