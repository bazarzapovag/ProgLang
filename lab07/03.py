t = int(input())
res = []
for i in range(t):
    a, b, c, d, e, f, g, h = map(int, input().split())

    ch1 = a * d + c * b
    zn1 = b * d

    ch2 = e * h + g * f
    zn2 = f * h

    left = ch1 * zn2
    right = ch2 * zn1

    if left < right:
        res.append('-1')
    elif left > right:
        res.append('1')
    else:
        res.append('0')
print(' '.join(res))
