s = input().strip()
words = s.split()
res = []

for word in words:
    obr_word = word[::-1]
    res.append(obr_word)

print(' '.join(res))
