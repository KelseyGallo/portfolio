# Program name: myFavoriteCars.py
# Program description: Sorts a list of car information
# Programmer's name: Kelsey Gallo
# Date: 2-4-25

car1 = (1999, 'Fiat', 500, 'white')
car2 = (2010, 'Volkswagen', 'Beetle', 'pink')
car3 = (2024, 'Toyota', 'Prius', 'silver')
cars = [car1, car2, car3]
for i in cars:
    print(i[0], i[3], i[1], i[2])

# When we refer to a string or tuple as "immutable," we mean that its value or values cannot be altered, added to, or removed. One
# advantage of using a tuple rather than a list is that a reader can know whether a sequence of values is not intended to be changed.
# Another advantage is that Python can optimize the code to process it more quickly if it uses tuples rather than lists.
