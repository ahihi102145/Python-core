n=int(input())
a=list(map(int,input().split()))
chan=[]
le=[]
for x in a:
    if x%2==0:
        chan.append(x)
    else:
        le.append(x)
if chan:
    print(*chan)
else:
    print("")
if le:
    print(*le)
else:
    print("")