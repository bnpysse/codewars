"""
Mark got a rectangular array matrix for his birthday, and now he's thinking about all the fun things he can do with it. He likes shifting a lot, so he decides to shift all of its i-contours in a clockwise direction if i is even, and counterclockwise if i is odd.

Here is how Mark defines i-contours:

the 0-contour of a rectangular array as the union of left and right columns as well as top and bottom rows;
consider the initial matrix without the 0-contour: its 0-contour is the 1-contour of the initial matrix;
define 2-contour, 3-contour, etc. in the same manner by removing 0-contours from the obtained arrays.
Implement a function that does exactly what Mark wants to do to his matrix.

Example

For

matrix = [[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16],
           [17, 18, 19, 20]]
the output should be

solution(matrix) = [[ 5,  1,  2,  3],
                     [ 9,  7, 11,  4],
                     [13,  6, 15,  8],
                     [17, 10, 14, 12],
                     [18, 19, 20, 16]]
For matrix = [[238, 239, 240, 241, 242, 243, 244, 245]],
the output should be
solution(matrix) = [[245, 238, 239, 240, 241, 242, 243, 244]].

Note, that if a contour is represented by a 1 × n array, its center is considered to be below it.

For

matrix = [[238],
           [239],
           [240],
           [241],
           [242],
           [243],
           [244],
           [245]]
the output should be

solution(matrix) = [[245],
                     [238],
                     [239],
                     [240],
                     [241],
                     [242],
                     [243],
                     [244]]
If a contour is represented by an n × 1 array, its center is considered to be to the left of it.
"""
# 应该按照 contours 来进行移动，找出最外圈，一圈一圈的向里，而不应该是原来的那种按方向进行转移的思路，那样太麻烦了
# 那么关键在于找出 contours，然后移动完了，需要再构造成原来的样子就可以了。
# 如果用这上面的方法试了一下，太复杂了，因为取出来的 up right down left会有重叠，然后行、列数不一样，还有逆序的问题
# 关键你写回去的时候，这些条件都需要考虑，实在是有些难办，还是考虑用 direction 的方案，这样比较直观
# 唯一的地方，是关于替换的问题，应该倒着开始，保留（0，0）位置的元素，然后从下一行的元素向上移
# 同样道理对于逆时针的情况，恰恰是从正方向开始的。2023-05-09 01:00:26

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]]
matrix = [[238],
          [239],
          [240],
          [241],
          [242],
          [243],
          [244],
          [245]]
matrix = [[238, 239, 240, 241, 242, 243, 244, 245]]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12]]
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
# matrix = [[1, 2, 3, 4, 5],
#           [6, 7, 8, 9, 10],
#           [11, 12, 13, 14, 15]]
clockwise = [((1, 0), (0, 1), (-1, 0), (0, -1)), ((0, 1), (1, 0), (0, -1), (-1, 0))]
# counterclockwise = ((0,-1),(1,0),(0,1),(-1,0))
rows = len(matrix)
cols = len(matrix[0])
tmp = matrix[0][0]
row = 0
col = 0
direct = 0
contours = min(rows, cols) // 2 if rows > 0 or cols > 0 else 0
cur_pos = row, col
cur_row, cur_col = 0, 0
for contour in range(contours):
    tmp = matrix[cur_row][cur_col]
    cur_pos = cur_row, cur_col
    direct = 0
    while direct < 4:

        next_pos = clockwise[contour % 2][direct][0] + cur_pos[0], clockwise[contour % 2][direct][1] + cur_pos[1]
        while cur_row <= next_pos[0] < rows - cur_row and cur_col <= next_pos[1] < cols - cur_col:
            matrix[cur_pos[0]][cur_pos[1]] = matrix[next_pos[0]][next_pos[1]]
            cur_pos = next_pos
            next_pos = clockwise[contour % 2][direct][0] + cur_pos[0], clockwise[contour % 2][direct][1] + cur_pos[1]
        direct += 1
    if contour % 2 == 0:
        matrix[contour][contour + 1] = tmp
    else:
        matrix[contour + 1][contour] = tmp
    cur_row += 1
    cur_col += 1
if rows == 1:
    matrix[0].insert(0, matrix[0].pop(-1))

if cols == 1:
    matrix.insert(0, matrix.pop())

# 这个地方的判断一直没有解决好，一开始考虑是与行数、列数的奇偶有关系，后来又考虑与 contour 有关系
# 其实想明白了就简单了，与行列无关，是与行列当中较小的值有关，如果较小的值为奇数，那么就会产生单行或者单列
# 再往下就简单了，行数多于列数，那么就按单列处理
# 列数多于行数，就按单行处理
if min(rows, cols) % 2 > 0:
    if rows > cols:
        # 得用循环完成，行数多，其实是单列多个元素的情况
        # 取出当前元素
        tmp = matrix[cur_row][cur_col]
        for r in range(cur_row, rows - contours * 2):
            matrix[r][cur_col] = matrix[r + 1][cur_col]
        matrix[rows - contours * 2][cur_col] = tmp
    else:
        # 这个其实是多列单行的情况，是列数多
        tmp = matrix[cur_row][cur_col]
        for c in range(cur_col, cols - contours * 2):
            matrix[cur_row][c] = matrix[cur_row][c + 1]
        matrix[cur_row][cols - contours * 2] = tmp
result = list()
for i in matrix:
    result.append(i)
print(result)