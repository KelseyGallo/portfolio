# Program name: workWithFiles3.py
# Program description: Reads a list of dog names and appends to a list of cat names
# Programmer's name: Kelsey Gallo
# Date: 2-17-25
# Define variables containing paths to dognames.txt and catnames.txt
dogFile="/cygdrive/c/cpt180stuff/pets/dogs/dognames.txt"
catFile="/cygdrive/c/cpt180stuff/pets/cats/catnames.txt"
# Check to see if both files exist
if [ -e $dogFile && -e $catFile ]
then
	 # Run the program
	 cat $dogFile # Display contents of dognames.txt
	 cat $catFile # Display contents of catnames.txt
	 echo -e "Pikachu \nJellylorum" >> $catFile # Add two names to catnames.txt
	 cat $catFile # Display contents of catnames.txt with added names
else
	 # Print error message
	 echo Unable to access one or more files
fi
# In Bash, the six indicators that can check for file attributes are -e, -r, -w, -x, -f, and -d. -e checks if a file exists, and -r, -w, and -x determine
# if it is readable, writable, or executable respectively. -f checks if the provided path is a regular file, and -d checks if it is a directory instead.