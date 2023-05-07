"""

The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

"""

matrix = [[43, 455, 32, 103], [102, 988, 298, 981], [309, 21, 53, 64], [2, 22, 35, 291]]
tmp = []
size = len(matrix)
for i in range(size):
    for j in range(size):
        if i == j:
            tmp.append(matrix[i][j])
for i in range(size):
    for j in range(size):
        if i == j:
            print(tmp)
            matrix[i][j] = tmp.pop()
tmp = []
for i in range(size):
    for j in range(size):
        if i + j == size-1:
            tmp.append(matrix[i][j])
for i in range(size):
    for j in range(size):
        if i + j == size-1:
            matrix[i][j] = tmp.pop()
print(matrix)
