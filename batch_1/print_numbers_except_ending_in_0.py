# A program that prints all numbers from 0 to 100 except those ending in 0.

for count in range(101):
    if count % 10:  
        print(count)