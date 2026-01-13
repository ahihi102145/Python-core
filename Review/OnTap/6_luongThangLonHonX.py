n=int(input())

employees=[]
for i in range(n):
    a=input().split()
    ten=a[0]
    ma=a[1]
    hsl=float(a[2])
    pc=int(a[3])
    luong=int(hsl*2000000+pc)
    employees.append((ma,ten,luong))

x = int(input().strip())

cnt=0
res=[]
for ma,ten,luong in employees:
    if luong > x:
        res.append((ma, ten, luong))
        cnt+=1
if cnt==0:
    print("Khong co nhan vien thoa man dieu kien")
else:
    print("So luong nhan vien co luong > {}: {}".format(x,cnt))
    for ma,ten,luong in res:
        print("{} {} {:.2f}".format(ma,ten,luong))