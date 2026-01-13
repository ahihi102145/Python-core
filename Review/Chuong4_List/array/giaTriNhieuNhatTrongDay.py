n = int(input())
a = list(map(int, input().split()))
fre = {}
for x in a:
    fre[x] = fre.get(x, 0) + 1
maxFre = -1
res = None
for x in fre:
    if fre[x] > maxFre or (fre[x] == maxFre and res > x):
        maxFre = fre[x]
        res = x

print(res)