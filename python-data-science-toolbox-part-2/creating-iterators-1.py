# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)


# Create an iterator for flash: superhero
# The iter method creates an iterator for the iterable passed to its argument
superhero = iter(flash)

# Print each item from the iterator
# The next method prints the next value of an iterator passed to its argument
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))