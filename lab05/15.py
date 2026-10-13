n = int(input())
cnt = 0

i = 0
while i < n:
    stoim, zatrat = map(int, input().split())
    pribil = stoim - zatrat
    if pribil > 0:
        cnt += pribil
    i += 1

print(cnt)
