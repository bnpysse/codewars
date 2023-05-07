canvas = [["a", "a", "a", "a", "a", "a", "a", "a"], ["a", "a", "a", "a", "a", "a", "a", "a"],
          ["a", "a", "a", "a", "a", "a", "a", "a"], ["b", "b", "b", "b", "b", "b", "b", "b"]]
rectangle = [0, 2, 7, 3]
x1, y1, x2, y2 = rectangle
w, h = x2 - x1 + 1, y2 - y1 + 1
# tmp = list()
# tmp.append('*')
# for i in range(x2 - x1 - 1): tmp.append('-')
# tmp.append('*')
# # 写入top
# for i in range(w):
#     canvas[y1][x1 + i] = tmp[i]
#     canvas[y1 + h - 1][x1 + i] = tmp[i]
# for i in range(1, h - 1):
#     canvas[x1 + i][y1] = '|'
#     canvas[x1 + i][y1 + w - 1] = '|'

# canvas[x1][y1] = "*"
# canvas[x2][y2] = "*"
# canvas[x1][y2] = "*"
# canvas[x2][y1] = "*"
# for i in range(x1 + 1, x2):
#     canvas[y1][i] = "-"
#     canvas[y1][i] = "-"
# for i in range(y1 + 1, y2):
#     canvas[i][x1] = "|"
#     canvas[i][x2] = "|"
#
# for i in canvas:
canvas[rectangle[1]][rectangle[0]] = "*"
canvas[rectangle[3]][rectangle[2]] = "*"
canvas[rectangle[1]][rectangle[2]] = "*"
canvas[rectangle[3]][rectangle[0]] = "*"
for i in range(rectangle[0] + 1, rectangle[2]):
    canvas[rectangle[1]][i] = "-"
    canvas[rectangle[3]][i] = "-"
for i in range(rectangle[1] + 1, rectangle[3]):
    canvas[i][rectangle[0]] = "|"
    canvas[i][rectangle[2]] = "|"
for i in canvas:
    print(i)
