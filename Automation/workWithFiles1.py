# Program name: workWithFiles1.py
# Program description: Lists contents of the CPT180Stuff folder
# Programmer's name: Kelsey Gallo
# Date: 2-11-25

from pathlib import Path
import os
print(Path.cwd()) # Lists the current working directory
os.chdir('C:\\cpt180stuff') # Changes to the CPT180Stuff folder
print(Path.cwd())
if os.path.exists('C:\\cpt180stuff\\cellphones') == False:
    os.makedirs('C:\\cpt180stuff\\cellphones') # Creates the Cellphones subfolder if it doesn't exist
print('The CPT180Stuff folder contains the following: ' + str(os.listdir('C:\\cpt180stuff'))) # Contents of CPT180Stuff
print('The CPT180Stuff\\cars folder contains the following: ' + str(os.listdir('C:\\cpt180stuff\\cars'))) # Contents of Cars subfolder
print('The CPT180Stuff\\pets folder contains the following: ' + str(os.listdir('C:\\cpt180stuff\\pets'))) # Contents of Pets subfolder
print('The CPT180Stuff\\pets\\cats folder contains the following:') # Contents and size of documents in Cats
for filename in os.listdir('C:\\cpt180stuff\\pets\\cats'):
    filesize = os.path.getsize(os.path.join('C:\\cpt180stuff\\pets\\cats', filename))
    print(filename + ': ' + str(filesize) + ' bytes')
print('The CPT180Stuff\\pets\\dogs folder contains the following:') # Contents and size of documents in Dogs
for filename in os.listdir('C:\\cpt180stuff\\pets\\dogs'):
    filesize = os.path.getsize(os.path.join('C:\\cpt180stuff\\pets\\dogs', filename))
    print(filename + ': ' + str(filesize) + ' bytes')

# The result of this code, on my Windows computer, would be C:\Users\Kelsey. The significance of this result is that it returns
# my home directory or home folder, where all of the files for my user account are stored on my computer.
