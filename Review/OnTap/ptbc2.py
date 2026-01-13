n=int(input())
cnt=0
for _ in range(n):
    ten,ma,dtb=input().split()
    dtb=float(dtb)
    if dtb>=8.0:
        cnt+=1
print(cnt)
