# Import reduce from functools
import functools
from functools import reduce


# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
# The reduce() function takes two arguments: a function, and a list
# It applies the function in the first argument on every element of the passed list
result = reduce((lambda item1, item2: item1 + item2), stark)

# Print the result
print(result)