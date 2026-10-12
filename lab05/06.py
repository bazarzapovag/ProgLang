n, m, k = map(int, input().split())

a = n * m
box = a // k
if a % k != 0:
    box= box + 1
print(box)
