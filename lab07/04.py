n = int(input())
nums = list(map(int, input().split()))

res = []
for x in nums:
    xd = bin(x)[2:]
    y = len(xd)
    yd = bin(y)[2:]
    z = len(yd)
    c = '0' * (z - 1) + yd + xd[1:]
    res.append(c)

print(''.join(res))
