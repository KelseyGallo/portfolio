# This program says hello and asks for my name.
print('Hello, world!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# In the last line of the program, there is the following snippet of code: str(int(myAge) + 1). "myAge" is the variable that stores
# the number that the user inputs for the age question. int() converts the number from a string to an integer for use in the
# mathematical equation myAge + 1. str() allows the resulting integer number to be evaluated into a string value, so that it can be
# passed into the print() function.
