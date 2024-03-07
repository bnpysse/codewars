def find_nb(m):
    # your code
    def n3(n):
        yield (n * (n + 1) // 2) * (n * (n + 1) // 2)

    n = 10
    n_val = 10000
    while n_val<=m:
        n_val = next(n3(n))
        n += 1
    return -1 if n>m else n

print(find_nb(4183059834009))