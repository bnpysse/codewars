"""
You are watching a volleyball tournament, but you missed the beginning of the very first game of your favorite team. Now you're curious about how the coach arranged the players on the field at the start of the game.

The team you favor plays in the following formation:

0 3 0
4 0 2
0 6 0
5 0 1
where positive numbers represent positions occupied by players. After the team gains the serve, its members rotate one position in a clockwise direction, so the player in position 2 moves to position 1, the player in position 3 moves to position 2, and so on, with the player in position 1 moving to position 6.

Here's how the players change their positions:

Given the current formation of the team and the number of times k it gained the serve, find the initial position of each player in it.

Example

For

formation = [["empty",   "Player5", "empty"],
             ["Player4", "empty",   "Player2"],
             ["empty",   "Player3", "empty"],
             ["Player6", "empty",   "Player1"]]
and k = 2, the output should be

solution(formation, k) = [
    ["empty",   "Player1", "empty"],
    ["Player2", "empty",   "Player3"],
    ["empty",   "Player4", "empty"],
    ["Player5", "empty",   "Player6"]
]
For

formation = [["empty", "Alice", "empty"],
             ["Bob",   "empty", "Charlie"],
             ["empty", "Dave",  "empty"],
             ["Eve",   "empty", "Frank"]]
and k = 6, the output should be

solution(formation, k) = [
    ["empty", "Alice", "empty"],
    ["Bob",   "empty", "Charlie"],
    ["empty", "Dave",  "empty"],
    ["Eve",   "empty", "Frank"]
]
这个处理的还是比较牛的，主要还是理解了题意，2023-05-07 15:20:04
一个是次数的变化，一个是利用了堆栈的思想，弹出并压入，实际上是一个循环队列的思路
具体讲，其实与矩阵没有什么实质性的关系。呵呵
"""
formation = [["empty", "Player5", "empty"], ["Player4", "empty", "Player2"], ["empty", "Player3", "empty"],
             ["Player6", "empty", "Player1"]]
k = 2
number = 2*k % 6
# 记录下初始位置
direct = [(-1, -1), (2, 0), (1, 1), (-1, 1), (-2, 0), (1, -1)]
origin_pos = [(3, 2), (1, 2), (0, 1), (1, 0), (3, 0), (2, 1)]
# pos记录下每次的变化
# 移动一次后，direct,origin_pos都将第一个元素弹出，并压入各自的尾部
pos = list()
for i in origin_pos:
    pos.append([i, formation[i[0]][i[1]]])
for j in range(number):
    for i in range(len(origin_pos)):
        new_pos = origin_pos[i][0] + direct[i][0], origin_pos[i][1] + direct[i][1]
        pos[i][0] = new_pos
    direct.append(direct.pop(0))
    origin_pos.append(origin_pos.pop(0))
for item in pos:
    formation[item[0][0]][item[0][1]] = item[1]
for i in formation:
    print(i)
