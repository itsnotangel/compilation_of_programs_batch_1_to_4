# A program that prints numbers without duplicates.
num_list = []

for count in range(10):
    num = float(input("Enter number " + str(count+1) + ": "))
    num_list.append(num)

print(num_list)
