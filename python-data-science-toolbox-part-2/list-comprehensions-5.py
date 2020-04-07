# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
# The output is a dictionary where the key is a member, and the value is the length of its name
new_fellowship = {member : len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)
