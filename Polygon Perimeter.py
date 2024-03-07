"""
You have a rectangular white board with some black cells.
The black cells create a connected black figure, i.e.
it is possible to get from any black cell to any other one through
connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For

matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
the output should be
solution(matrix) = 12.



For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
the output should be
solution(matrix) = 16.

确定出一个 True 单元格四个方向的位置，如果 ①超出矩阵范围的 ②为False值的，进行过滤，并统计其个数即可。
2023-05-09 22:03:38
"""
from typing import Callable, Any, Union

matrix_example = [[True, True, True],
                  [True, False, True],
                  [True, True, True]]


def solution(matrix):
    direct = ((-1, 0), (0, 1), (1, 0), (0, -1))
    s = 0
    rows = len(matrix)
    cols = len(matrix[0])
    new_pos: Callable[[Any], tuple[Union[int, Any], Union[int, Any]]] = lambda x: (r + x[0], c + x[1])
    filter_condition: Callable[[Any], bool] = lambda x: not (0 <= x[0] < rows and 0 <= x[1] < cols) or \
        not matrix[x[0]][x[1]]
    for r in range(len(matrix)):
        c: int
        for c in range(len(matrix[0])):
            if matrix[r][c]:
                s += len(list(filter(filter_condition, map(new_pos, direct))))
    print(s)


solution(matrix_example)
