n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
maxVal=a[0]
check=0
res=0
for  x in a:
    if x!=maxVal:
        res=x
        check=1
        break
if check==1:
    print(res)
else:
    print(-1)