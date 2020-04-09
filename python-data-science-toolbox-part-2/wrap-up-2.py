# row_lists is a list of lists
# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# lists2dict is defined in wrap-up-1.py
# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])