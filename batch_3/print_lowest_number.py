# A program that asks the user to input a number, continues asking until the input is invalid, and displays the lowest number.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        print("Invalid")
        break