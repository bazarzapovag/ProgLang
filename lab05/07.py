import math

n, t = input().split()
n = int(n)
t = float(t)

res = n * 60 / t
print(math.ceil(res))
