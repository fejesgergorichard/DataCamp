# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
# The filter() function takes two arguments: a function and a list
# This function returns a filtered list with the elements that were evaluated 'True' by the passed function
result = filter(lambda a: len(a) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Print result_list
print(result_list)