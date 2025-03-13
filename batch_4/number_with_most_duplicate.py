#  A program that keeps asking the user for a number until they enter an invalid input. Then, show the number that appeared the most.

num_list = []
while True:
    try:
        num = float(input("Enter a number: "))
        num_list.append(num)
    except ValueError:
        break
    
if num_list:
    mode = max(set(num_list), key=num_list.count)
    print(mode)