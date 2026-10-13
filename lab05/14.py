n = int(input())
masha = 0
dasha = 0

i = 0
while i < n:
    num = int(input())
    if num % 3 == 0:
        masha += 2
    else:
        dasha += 1
    i += 1

print(f"{masha}:{dasha}")
