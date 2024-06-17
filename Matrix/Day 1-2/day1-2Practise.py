# Practice Exercise:
# 1. Write a function print_matrix(matrix) that prints each row of a given matrix on a new line, 
# demonstrating your understanding of matrix representation and access.

def print_matrix(matrix):
    for r in range(len(matrix)):
        print(matrix[r])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print_matrix(matrix)
#Output: [1, 2, 3]
#        [4, 5, 6]
#        [7, 8, 9]

# 2. a) Find all main diagonal elements of the matrix and 
#    b) anti-diagonal elements of the matrix

# a) to find all main diagonal elements i.e. 1,5,9 we have to iterate through all rows and columns 
# (0,0), (1,1), (2,2) 
#approach 1: check if r and c are equal
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if r == c:
            print(matrix[r][c])

#approach 2: Check if the column index is within bounds
# Iterate through rows
for i in range(len(matrix)): 
    if i < len(matrix[i]):  #0 < 3, 1< 3, 2< 3
        print(matrix[i][i]) #0,0 1,1 2,2

# b) to find all anti diagonal elements i.e. 3,5,7 
# (0,2) (1,1) (2,0) - check if sum of r + c == rows - 1 i.e. here 3 -1 = 2
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if i + j == rows - 1:
            print(matrix[i][j])