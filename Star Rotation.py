"""

Consider a (2k+1) × (2k+1) square subarray of an integer integers matrix. Let's call the union of the square's two longest diagonals, middle column and middle row a star. Given the coordinates of the star's center in the matrix and its width, rotate it 45 · t degrees clockwise preserving position of all matrix elements that do not belong to the star.
考虑一个整数矩阵的 (2k+1) × (2k+1) 方形子数组。让我们将正方形的两条最长对角线（中间列和中间行）的并集称为星形。给定星星的 center 在 matrix 及其 width 中的坐标，将其顺时针旋转 45 · t 度，保留所有不属于星星的矩阵元素的位置。

Example 例子

For 为了

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0],
          [0, 7, 0, 6, 0, 5, 0],
          [7, 0, 0, 6, 0, 0, 5]]
width = 7, center = [3, 3], and t = 1, the output should be
width = 7 、 center = [3, 3] 和 t = 1 ，输出应该是

solution(matrix, width, center, t) = [[8, 0, 0, 1, 0, 0, 2],
                                          [0, 8, 0, 1, 0, 2, 0],
                                          [0, 0, 8, 1, 2, 0, 0],
                                          [7, 7, 7, 9, 3, 3, 3],
                                          [0, 0, 6, 5, 4, 0, 0],
                                          [0, 6, 0, 5, 0, 4, 0],
                                          [6, 0, 0, 5, 0, 0, 4]]
For 为了

matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0]]
width = 3, center = [1, 5], and t = 81, the output should be
width = 3 、 center = [1, 5] 和 t = 81 ，输出应该是

solution(matrix, width, center, t) = [[1, 0, 0, 2, 0, 0, 0],
                                          [0, 1, 0, 2, 3, 3, 3],
                                          [0, 0, 1, 2, 0, 0, 0],
                                          [8, 8, 8, 9, 4, 4, 4],
                                          [0, 0, 7, 6, 5, 0, 0]]
"""
matrix = [[1, 0, 0, 2, 0, 0, 3],
          [0, 1, 0, 2, 0, 3, 0],
          [0, 0, 1, 2, 3, 0, 0],
          [8, 8, 8, 9, 4, 4, 4],
          [0, 0, 7, 6, 5, 0, 0],
          [0, 7, 0, 6, 0, 5, 0],
          [7, 0, 0, 6, 0, 0, 5]]
width = 7
center = [3, 3]
t = 1
# 起始点即为中心点均减一，为(2,2)
# 圈数 circle = (width - 3) // 2 + 1,最小的就是3维的，不能比3维再小了。即要循环两层，最内层是3×3，然后是5×5...
# 起始位置 center - 1 - 圈数的循环量
# 移动的位置是 direct*circle ,也就是说最内层的不动
# 如果大一圈，扩大一倍 *1 *2 *3...
direct = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)]
# s = 2
circle = (width - 3) // 2 + 1
for t1 in range(t % 8):
    for s in range(circle):
        pos = list(map(lambda x: (x[0] + center[0] - 1 - s, x[1] + center[1] - 1 - s),
                       map(lambda x: (x[0] * (s + 1), x[1] * (s + 1)), direct)))
        print(pos)
        tmp = matrix[pos[-1][0]][pos[-1][1]]
        for i in range(-1, -len(pos), -1):
            matrix[pos[i][0]][pos[i][1]] = matrix[pos[i - 1][0]][pos[i - 1][1]]
        matrix[pos[0][0]][pos[0][1]] = tmp
for i in matrix: print(i)
