n, m, c, k = map(int, input().split())
a = n * m - k

if a <= 0:
    print(0)
else:
    pach = a // 200
    if a % 200 != 0:
        pach = pach + 1
    price = pach * c
    print(price)
