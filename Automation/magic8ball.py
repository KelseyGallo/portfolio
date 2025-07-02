# Program name: magic8ball.py
# Program description: Simulates a Magic 8 Ball based on a random number
# Programmer's name: Kelsey Gallo
# Date: 1-28-25

import random

print('What is your name?') # Asks for the user's name
name = input()

print ('What is your yes/no question?') # Asks for a yes/no question
input()

def getAnswer(answerNumber): # Assigns answers based on generated numbers
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    elif answerNumber == 10:
        return 'Not a chance!'

r = random.randint(1, 10) # Randomly generates a number between 1 and 10
fortune = getAnswer(r) # Fortune is the answer that corresponds to the number
print(name + ', ' + fortune) # Prints the user's name and their fortune

# Python's two levels of scope are local and global. The local scope refers to parameters and variables that only exist in a certain
# function. This scope lasts from the time a function is created to the time it is called, and the values are reset the next time
# the user calls the function. The global scope include variables assigned outside of all of the functions in the program, and exists
# for as long as the program runs. Variables in the global scope apply to the entire program unless defined otherwise by a function.
