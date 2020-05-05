for n in range(1, 201):
    prastevila = []
    for d in range(2, n):
        if n % d == 0:
            break
    else:
        print(n)

