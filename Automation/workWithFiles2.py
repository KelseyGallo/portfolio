# Program name: workWithFiles2.py
# Program description: Reads a list of dog names and appends to a list of cat names
# Programmer's name: Kelsey Gallo
# Date: 2-11-25

from pathlib import Path
import os

dogFile = Path('C:\\cpt180stuff\\pets\\dogs\\dognames.txt')
catFile = Path('C:\\cpt180stuff\\pets\\cats\\catnames.txt')

def program():
    dogNames = open(dogFile)
    dogContent = dogNames.read()
    dogNames.close()
    print(dogContent)
    catNames = open(catFile)
    catContent = catNames.read()
    catNames.close()
    print(catContent)
    catNames = open(catFile, 'a')
    catContent = catNames.write('Zzyzx\nSnufflekins\n')
    catNames.close()
    catNames = open(catFile)
    catContent = catNames.read()
    catNames.close()
    print(catContent)
    
if os.path.exists(dogFile) == True and os.path.exists(catFile) == True:
    program()
else:
    print('Unable to access one or more files.')

# The read() method returns a text file's contents as a single string, while the readlines() method gives the contents as a list
# of strings, with each line separated by the \n newline character.
    
    
