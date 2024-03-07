"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.
在流行的扫雷游戏中，您有一个带有一些地雷的棋盘，那些不包含地雷的单元格中有一个数字，表示相邻单元格中的地雷总数。从布置地雷开始，我们想要创建一个扫雷游戏设置。

Example 例子

For 为了

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be 输出应该是

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
"""
from typing import Callable, Any, Union

matrix = [[True, False, False, True],
          [False, False, True, False],
          [True, True, False, True]]
direct = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
rows = len(matrix)
cols = len(matrix[0])
in_range: Callable[[Any], Union[bool, Any]] = lambda x: 0 <= x[0] < rows and 0 <= x[1] < cols
stack = list()
for r in range(rows):
    for c in range(cols):
        # pos = list(map(lambda x:(r+x[0],c+x[1]),direct))
        # 这里的这个操作，如果不作说明的话，可能过一天自己都看不懂了，哈哈，2023-05-08 11:20:13
        # 最里层的，是先累加得到每个坐标的周围八个方向的坐标
        # 然后是过滤掉不符合范围的
        # 然后把这个符合范围的坐标对，取到对应的 matrix 中的值
        # 然后计算这个符合条件的列表中 True 的个数
        stack.append(list(
            map(lambda x: matrix[x[0]][x[1]], filter(in_range, map(lambda x: (r + x[0], c + x[1]), direct)))).count(
            True))
print(stack)
# 将一维数组转二维数组，这个也比较牛逼！！2023-05-08 11:18:27
print([stack[i:i + cols] for i in range(0, len(stack), cols)])
