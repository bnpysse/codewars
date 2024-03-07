s, n = "!!!Hi !!hi!!! !hi", 5
s,n = "!!!Hi !!hi!!! !hi",3
s,n = "Hi!",1
r = [[ch for ch in item] for item in s.split(' ')]
cnt = 0
result = []
for item in r:
    while '!' in item and cnt<n:
        item.remove('!')
        cnt += 1
    result.append(''.join(item))

print(' '.join(result))
