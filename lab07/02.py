t = int(input())
for i in range(t):
    n = int(input())
    p, q = map(int, input().split())
    
    res= []
    for i in range(n):
        p *= 2
        if p >= q:
            res.append('1')
            p -= q
        else:
            res.append('0')
    
    print('0.' + ''.join(res))
