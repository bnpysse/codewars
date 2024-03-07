rooms, need = [['XXXXXXX', 6], ['', 1], ['XXX', 1], ['XXXXXXXXXX', 9], ['XXXXX', 6], ['XXX', 10], ['', 1],
               ['XXXXXXXXX', 5]], 7
l = [num - len(chair) if num - len(chair) > 0 else 0 for chair, num in rooms]
def solve(l,need):
    cnt = 0
    res = []
    for k, v in enumerate(l):
        cnt += v
        if cnt < need:
            res.append(v)
            continue
        elif cnt == need:
            break
        else:
            v = v - (cnt - need)
            res.append(v)
            break
    return res
f'Not enough!'if sum(l:=[num-len(chair) if num-len(chair)>0 else 0 for chair,num in rooms])<need \
     else f'Game On' if need == 0 else solve(l,need)
