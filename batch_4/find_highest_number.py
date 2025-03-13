# Create a program that ask user to input a number.
# Continue asking until the user input is invalid. 
# Display the highest number.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        print("Invalid")
        break

if num_list:
    print("The highest number is:", max(num_list))