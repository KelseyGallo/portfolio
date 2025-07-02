# Program name: printRandomNumbers.py
# Program description: Generates a list of random numbers from user input
# Programmer's name: Kelsey Gallo
# Date: 1-21-25

import random
print('Enter number of random numbers needed.') # Asks for the number of random numbers in the list
number = int(input())
print('Enter the lower limit.') # Asks for the lower limit of the numbers
low = int(input())
print('Enter the upper limit.') # Asks for the upper limit of the numbers
high = int(input())
print(' ')
for i in range(number):
    print(random.randint(low, high), end=" ") # Generates the list

# When importing a module into a Python program, using the import statement requires typing the module's prefix when calling its
# functions, which is not necessary when using the from statement. The import statement is normally preferred, however, because
# it allows the user to identify the modules used in the function when reading the code.
