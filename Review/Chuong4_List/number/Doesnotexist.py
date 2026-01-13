n = int(input())
a = list(map(int, input().split()))
fre = {}
for x in a:
    fre[x] = fre.get(x, 0) + 1
res = []
for x in a:
    if fre[x] == 1:
        res.append(x)
if res:
    print(*res)

else:
    print("Does not exist")