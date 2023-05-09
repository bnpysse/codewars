"""
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.
数独是一种数字拼图游戏。目标是用数字填充 9 × 9 网格，以便组成该网格的每一列、每一行和九个 3 × 3 子网格中的每一个都包含从 1 到 9 的所有数字。

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
该算法应检查给定的数字网格是否代表数独的正确解决方案。

Example 例子

For 为了
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be 输出应该是
solution(grid) = true;  solution(grid) = true ；

For 为了
grid = [[8, 3, 6, 5, 3, 6, 7, 2, 9],
        [4, 2, 5, 8, 7, 9, 3, 8, 1],
        [7, 9, 1, 2, 1, 4, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be 输出应该是
solution(grid) = false.  solution(grid) = false 。

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
输出应为 false ：九个 3 × 3 子网格中的每一个都应包含从 1 到 9 的所有数字。
"""
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
# 获取每行
r = [row for row in grid]
# 获取每列
c = [row[x] for x in range(9) for row in grid]
# 获取子矩阵
for y in range(0, 9, 3):
        print([r[x:x + 3] for x in range(0, 9, 3) for r in grid[y:y + 3]])
