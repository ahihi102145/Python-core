import math
def soChinhPhuong(n):
    res=int(math.sqrt(n))
    if res*res==n:
        return 1
    return 0

a,b=map(int,input().split())
cnt=0
for i in range(a,b+1):
    if soChinhPhuong(i):
        cnt+=1
print(cnt)