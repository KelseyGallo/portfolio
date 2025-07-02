# Program name: vampire.py
# Program description: Asks for a user's name and age
# Programmer's name: Kelsey Gallo
# Date: 1-21-25

print('What is your name?') # Asks for the user's name
name = input()
print('What is your age?') # Asks for their age in years
age = int(input())
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are not Alice.')

# if car = 'Ford':
#    print('You have a Ford.')
# elif car = 'Chevrolet':
#    print('You have a Chevrolet.')
