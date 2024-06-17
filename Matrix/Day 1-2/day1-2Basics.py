# Day 1-2: Understanding Matrices in Python

# Learn how to represent matrices using lists of lists in Python.
# Practice accessing elements and understanding matrix dimensions.

# Day 1: Representing, Accessing  Matrices in Python
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Matrix Representation:
# In Python, matrices are commonly represented using nested lists. Each inner list represents a row of the matrix. 
# Here's how you can define a matrix:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

#Irregular matrix
# matrix = [
#     [1, 2],
#     [4, 5, 6],
#     [1]
# ]

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Accessing Elements:
# You can access elements of the matrix using indices. Remember that indexing in Python starts from 0.

# [1, 2, 3] -> [(0,0), (0,1), (0,2)]
# [4, 5, 6] -> [(1,0), (1,1), (1,2)]
# [7, 8, 9] -> [(2,0), (2,1), (2,2)]
elements = matrix[1][2]
print(elements) # Output: 6

# Day 2: Understanding Matrix Dimensions
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Finding Matrix Dimensions:
# To find the dimensions (number of rows and columns) of a matrix, use the len() function:

rows = len(matrix)
cols = len(matrix[0])

print(f"Rows: {rows}, Columns: {cols}") #Output: Rows: 3, Columns: 3
