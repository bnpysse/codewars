fib = lambda n: 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)
l = [(i, fib(i) * fib(i + 1)) for i in range(1, 20)]
prod = 4895
for item in l:
    while item[1] <= prod:
        break
    if item[1] == prod:
        print(item[1], item[0], item[0] + 1)
        break
    elif item[1] > prod:
        print(item[1], item[0], item[0] + 1)
        break