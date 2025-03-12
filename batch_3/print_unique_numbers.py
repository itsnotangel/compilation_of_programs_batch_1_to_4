# A program that prints numbers without duplicates.
num_list = []

for count in range(10):
    num = float(input("Enter number " + str(count+1) + ": "))
    num_list.append(num)

unique_num = [num for num in num_list if num_list.count(num) == 1]

print(unique_num)
