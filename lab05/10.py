s = input().strip()
res = []
for ch in reversed(s):
    if ch == '(':
        res.append(')')
    else:
        res.append('(')
print(''.join(res))
