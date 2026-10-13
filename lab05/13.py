n = int(input())
cnt= 0
d = 1
while d < n:
    if n % d == 0:
        cnt+= d
    d += 1
print(cnt)
