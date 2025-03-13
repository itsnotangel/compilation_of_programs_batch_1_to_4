#  A program that keeps asking the user for a number until they enter an invalid input. Then, show the number that appeared the most.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break

if num_list:
    frequent_num = max(set(num_list), key=num_list.count)

    if num_list.count(frequent_num) == 1:
        print("No duplicates.")
    else:
        print("The number with most duplicate:", frequent_num)
else:
    print("Invalid input.")