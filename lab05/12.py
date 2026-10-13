a = input().split()
for x in a:
    n = int(x)
    d = 2
    while n % d != 0:
        d += 1
    print(d, end=' ')
