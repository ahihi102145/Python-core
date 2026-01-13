n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
maxVal=a[0]
found=0
for i in range(1,n):
    if a[i] != maxVal:
        print(a[i])
        found=1
        break
if not found:
    print(-1)
