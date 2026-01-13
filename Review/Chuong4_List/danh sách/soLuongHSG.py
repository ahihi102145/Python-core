n=int(input())
maxVal=-1e9
cnt=0
for i in range(n):
    a=input().split()
    ten=a[0]
    ma=a[1]
    dtb=float(a[2])
    if dtb>= 8.0:
        cnt+=1
print(cnt)