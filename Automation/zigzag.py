# Program name: zigzag.py
# Program description: Creates a zigzag pattern with asterisks until the keyboard interrupts it
# Programmer's name: Kelsey Gallo
# Date: 1-30-25

import time, sys

def runZigzag():
    indent = 0 # How many spaces to indent
    indentIncreasing = True # Whether the indentation is increasing or not
    try:
        while True: # The main program loop
            print(' ' * indent, end='')
            print('*' * int(number))
            time.sleep(0.1) # Pause for 1/10 of a second.

            if indentIncreasing:
                # Increase the number of spaces:
                indent = indent + 1
                if indent == 20:
                    # Change direction:
                    indentIncreasing = False

            else:
                # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
                    # Change direction:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()

while True:
    print('Enter an integer between 5 and 25.') # Asks the user for the number of asterisks per line
    try:
        number = input()
        if int(number) >= 5 and int(number) <= 25:
            break # Input is accepted, and the program begins
        elif int(number) < 5:
            print('The integer is too low.')
            continue
        elif int(number) > 25:
            print('The integer is too high.')
            continue
    except ValueError: # Input is not an integer, i.e. letters or a decimal
        print('You must enter an integer.')
        continue
    

runZigzag()

# Summer
# Winter
# Summer
# Summer
