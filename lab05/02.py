s = input().strip()
pol = len(s) // 2
lef= int(s[:pol])
rig= int(s[pol:])
print(lef+ rig)
