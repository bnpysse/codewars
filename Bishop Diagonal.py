"""
In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

Example

For bishop1 = "d7" and bishop2 = "f5", the output should be
solution(bishop1, bishop2) = ["c8", "h3"].



For bishop1 = "d8" and bishop2 = "b5", the output should be
solution(bishop1, bishop2) = ["b5", "d8"].

The bishops don't belong to the same diagonal, so they don't move.
"""
bishop1 = "d7"
bishop2 = "f5"

# 定义一个计算位置的 lambda 函数
pos = lambda p: (ord(p[0]) - ord('a'), int(p[1]) - 1)

pos1 = ord(bishop1[0]) - ord('a'), int(bishop1[1]) - 1
pos2 = pos(bishop2)

# 在棋盘上的对角线的四个方向，左上，右上，右下，左下
direct = ((1, -1), (1, 1), (-1, -1), (-1, 1))

# 计算在direct k中的方向
# 参数是两个位置的差，说明往哪个方向走，也就是在 direct 当中的索引值
dir_p = lambda x, y: ((1, -1)[x < 0], (1, -1)[y < 0])

# 相对方向，因为对角线是四个相对的方向
# 参数是 direct 当中的下标索引，传进1来就返回3，传进2来就返回0
face_dir_p = lambda p: (p - 2) % 4 if p > 2 else (p + 2) % 4

# 计算 pos1 的相对方向
diff = pos1[0]-pos2[0],pos1[1]-pos2[1]
# 也就是说，pos1要按照 (1,1) 的方向向左上加
move_pos1 = (face_dir_p(direct.index(dir_p(diff[0],diff[1]))))

# 同样道理，pos2 的移动方向为 pos1 的相对方向
move_pos2 = face_dir_p(move_pos1)

