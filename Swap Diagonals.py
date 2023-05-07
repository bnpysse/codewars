matrix = [[34, 1000, 139, 248, 972, 584], [98, 1, 398, 128, 762, 654], [33, 498, 132, 543, 764, 43],
          [329, 12, 54, 764, 666, 213], [928, 109, 489, 71, 837, 332], [93, 298, 42, 53, 76, 43]]

size = len(matrix)
# for r in range(len(matrix) // 2):
# 通常都是用这种方式来遍历，结果造成了内层循环多运行了，就会改变其他位置的值。
r = 0
for c in range(len(matrix) // 2):
    tmp = matrix[r][c]
    matrix[r][c] = matrix[r][size - c - 1]
    matrix[r][size - c - 1] = tmp
    r += 1
r = size // 2
# for r in range(len(matrix) // 2, size):
for c in range(len(matrix) // 2 - 1, -1, -1):
    tmp = matrix[r][c]
    matrix[r][c] = matrix[r][size - c - 1]
    matrix[r][size - c - 1] = tmp
    r += 1
print(matrix)
