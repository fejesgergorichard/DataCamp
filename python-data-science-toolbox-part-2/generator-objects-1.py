# A generator object is similar to a list comprehension, but it is defined by ( ) , not by [ ]
# This object, unlike the list comprehensions, does not create the list. It produces a generator
# The generator can be called as an iterable, and generates the required values on the fly, thus saving memory

# Create generator object: result
result = (num for num in range(31))

# Print the first 5 values
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# Print the rest of the values
for value in result:
    print(value)
