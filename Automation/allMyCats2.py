# Program name: allMyCats2.py
# Program description: Store a list of any number of cat names
# Programmer's name: Kelsey Gallo
# Date: 2-4-25

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input() # Adds a name to the list
    if name == '': # Ends the list if the enter key is pressed
        break
    catNames = catNames + [name] # list concatenation
catNames.sort() # Sorts the names in the list alphabetically
print('The cat names are:') # Displays the list
for name in catNames:
    print(' ' + name)

# myColor = orange ; string
# yourColors = ['blue', 'purple', 'yellow'] ; list
# thoseColors = ['purple', 'yellow', 'orange'] ; list
# allColors = 6 ; integer
