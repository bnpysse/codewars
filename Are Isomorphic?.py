"""
Two two-dimensional arrays are isomorphic if they have the same number of rows and each pair of respective rows contains the same number of elements.

Given two two-dimensional arrays, check if they are isomorphic.

Example

For

array1 = [[1, 1, 1],
          [0, 0]]
and

array2 = [[2, 1, 1],
          [2, 1]]
the output should be
solution(array1, array2) = true;

For

array1 = [[2],
          []]
and

array2 = [[2]]
the output should be
solution(array1, array2) = false.
"""
array1= [[], [1]]
array2= [[], [6,2,5]]
result = True
if len(array1) == len(array2):
    for row in range(len(array1)):
        if len(array1[row]) == len(array2[row]):
            continue
        else:
            result = False
else:
    result = False
print(result)