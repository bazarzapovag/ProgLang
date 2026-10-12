s = input().strip()

if '.' in s:
    rub, kop = s.split('.')
else:
    rub, kop = s, ''
if kop == '':
    kop = 0
elif len(kop) == 1:
    kop = int(kop) * 10
else:
    kop = int(kop)

print(f"{int(rub)} rub {kop} kop")
