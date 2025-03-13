# A program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        print("Invalid")
        break
    
if num_list:
    print("Descending order:", num_list)