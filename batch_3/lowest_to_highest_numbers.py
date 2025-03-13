# A program that asks the user to input a number, continues asking until the user input is invalid. 
# Displays the numbers from lowest to highest.

num_list = []

while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break

num_list.sort()  

print("Ascending order:", num_list)