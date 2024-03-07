objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
objC = {'a': 5, 'd': 11, 'e': 8}
objD = {'c': 3}
lst = {'a': 10, 'b': 20, 'c': 30}, {'a': 3, 'c': 6, 'd': 3}, {'a': 5, 'd': 11, 'e': 8}
res = dict()
for item in lst:
    for i in item.items():
        if i in res:
            print(i)
            res.update(i)
        else:
            res.setdefault(i)
print(res)