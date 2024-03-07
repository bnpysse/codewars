from itertools import combinations
p1 = 'rock'
p2 = 'scissors'
games = ['scissors', 'paper', 'rock']
result = ''
if p1 == p2:
    result = f'Draw!'
else:
    if p1 in ('scissors', 'rock') and p2 in ('scissors', 'rock'):
        result = 'Play 2 won!' if p1 == 'scissors' and p2 == 'rock' else 'Play 1 won!'
    if p1 in ('paper', 'rock') and p2 in ('paper', 'rock'):
        result = 'Play 1 won!' if p2 == 'paper' and p2 == 'rock' else 'Play 2 won!'
    if p1 in ('paper', 'scissors') and p2 in ('paper', 'scissors'):
        result = 'Play 1 won!' if p1 == 'scissors' and p2 == 'paper' else 'Play 2 won!'
    print(p1, p2)
print(result)