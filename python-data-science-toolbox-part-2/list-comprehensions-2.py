
# Nested for loop
# [col for col in range(0,5)] is creating a single row, which columns are filled with the value of 'col' in the range of 0-4
# ...for row in range(0,5) is making the [col for col in range(0,5)] part equal to 'row' and iterates it in the range of 0-4
# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
