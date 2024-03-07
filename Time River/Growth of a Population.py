p0, percent, aug, p = 1500,5,100,5000
for n in range(30):
    p0 = p0*(1+percent/100) + aug
    if p0>p:
        print(n)
        break