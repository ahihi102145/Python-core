
n=int(input())
res=[]
maxVal=-1e18
for i in range(n):
    a=input().split()
    ma=a[0]
    ten=a[1]
    cs1=float(a[2])
    cs2=float(a[3])
    cs3=float(a[4])
    tong = cs1+cs2+cs3
    res.append((ma, ten, tong))
    if tong > maxVal:
        maxVal=tong

for ma,ten,tong in res:
    if tong==maxVal:
        print("{} {} {:.2f}".format(ma,ten,tong))

