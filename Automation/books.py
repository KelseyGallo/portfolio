# Program name: books.py
# Program description: Creates a list of book titles and authors
# Programmer's name: Kelsey Gallo
# Date: 2-4-25

books = ['Frankenstein', 'David Copperfield', 'Brave New World', 'Moby Dick', 'Little Women']
authors = []
while True:
    for item in books:
        print('Who wrote ' + item + '?') # Asks who wrote each book
        author = input() # Adds an author to the list
        authors = authors + [author] # list concatenation
    break
print('The book titles and authors are:') #Displays the list of book titles and authors
for item, author in zip(books, authors): # Connects the two lists
    print(item + ' - ' + author)

# ['orange', 'yellow', 'purple', 'brown', 'green']
