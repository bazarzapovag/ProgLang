import math

x, y = map(float, input().split())
res = math.floor(y) - math.ceil(x) + 1
print(res)
