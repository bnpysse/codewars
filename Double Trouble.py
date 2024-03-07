def trouble(x, t):
    if len(x) == 1:
        return x
    elif (l:=[(k+1,v)for k,v in enumerate(zip(x,x[1:])) if v[0]+v[1]==t]):
        a,b = l.pop(0)
        x.pop(a)
        return trouble(x,t)
    else:
        return x
x = [9, 5, 9, 9, 4, 1, 8, 5, 2, 4, 7, 9, 8, 7, 8, 3, 1, 9, 1, 8, 7, 8, 9, 6, 7, 3, 8, 9, 9, 8]
t = 9
res = trouble(x, t)
print(res)