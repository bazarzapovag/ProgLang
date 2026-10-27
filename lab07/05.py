code = input().strip()
i = 0
numbers = []

while i < len(code):
    zero = 0
    while code[i] == '0':
        zero += 1
        i += 1

    z = zero + 1
    yd = code[i : i + z]
    y = int(yd, 2)
    i += z

    xd = code[i : i + y - 1]
    i += y - 1

    x = int('1' + xd, 2)
    numbers.append(x)

print(len(numbers))
print(' '.join(map(str, numbers)))
