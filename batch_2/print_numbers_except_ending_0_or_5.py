# A program that prints all numbers from 0 to 100 except those ending in 0 and 5.

for num in range(101):
    if num % 5 != 0:  
        print(num)