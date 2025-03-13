# A program that prompts the user to input a number and checks if it's unique or a duplicate.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        if num in num_list:
            print("Duplicate")
        else:
            print("Unique")
            num_list.append(num)
    except ValueError:
        print("Invalid input.")
        break