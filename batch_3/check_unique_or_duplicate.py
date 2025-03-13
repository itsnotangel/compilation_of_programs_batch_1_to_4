# A program that prompts the user to input a number and checks if it's unique or a duplicate. 
# For invalid inputs, it prints "Invalid" and exits the program.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
        print(num_list)
    except ValueError:
        print("Invalid")
        break


