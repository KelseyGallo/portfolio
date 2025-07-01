# Program name: ball.py
# Program description: Calcuates the volume of a ball using a given radius
# Programmer's name: Kelsey Gallo
# Date: 1-16-2025
print('What is your name?') # Asks for the user's name
name = input()
print('What is the color of the ball?') # Asks for the ball's color
color = input()
print('What is the radius of the ball?') # Asks for the ball's radius
radius = input()
pi = 3.1415926535897931
volume = 4/3 * pi * float(radius)**3 # Calculates the ball's volume
print('Hello ' + name + ", the ball is " + color + " and has a volume of " + str(round(volume, 2)) + " cubic inches.")
# Number values that are obtained from the user using the input() method cannot be directly used in a mathematical expression,
# because the user's input is always treated as a string, even if the input is a number. In order for the input to be used in
# this case, the associated variable must be converted into an integer using the int() function.
