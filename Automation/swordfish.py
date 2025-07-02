# Program name: swordfish.py
# Program description: Asks for a name and password
# Programmer's name: Kelsey Gallo
# Date: 1-21-25

while True:
    print('Who are you?') # Asks for the user's name
    name = input()
    if name != 'Joe' and name != 'Natalie':
        continue # Re-asks the question if the user's name is not Joe or Natalie
    print('Hello, ' + name + '. What is the password? (It is a fish.)') # If the user's name is Joe or Natalie, recognizes the user by name and asks for the password
    password = input()
    if password == 'swordfish':
        break # Correct password guessed
print('Access granted.')
# Prints uppercase letters
for letter in range(65, 91):
    print(chr(letter), end=" ")

# When used within a while loop, a continue statement immediately jumps back to the loop's start and begins a new iteration of the
# loop. A break statement, however, ends the loop entirely if the condition is true.
