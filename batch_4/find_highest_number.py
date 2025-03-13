# Create a program that ask user to input a number.
# Continue asking until the user input is invalid. 
# Display the highest number.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
        print(num_list)
    except ValueError:
        print("Invalid")
    break