s = input()
cnt = 0
for i in s:
    if i.isdigit():
        cnt += int(i)
print(cnt)
