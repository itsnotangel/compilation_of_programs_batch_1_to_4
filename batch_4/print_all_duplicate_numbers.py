# A program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

num_list = []

for count in range(10):
    num = float(input("Enter number " + str(count + 1) + ": "))
    num_list.append(num)

duplicate_num = list(set([num for num in num_list if num_list.count(num) > 1]))

print(duplicate_num)