a=list(map(int,input().split()))
res=[]
seen = set()
for x in a:
    if x not in seen:
        res.append(x)
        seen.add(x)
print(*res)