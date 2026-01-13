n=int(input())
cnt=0

HocLai = []
for i in range(n):
    a=input().split()
    name = a[0]
    ma = int(a[1])
    d1 = float(a[2])
    d2 = float(a[3])
    d3 = float(a[4])
    dtb = (d2+d1+d3)/3
    check = 0
    if d1 < 4.0:
        check+=1
    if d2 < 4.0:
        check+=1
    if d3 < 4.0:
        check+=1
    if check >= 2:
        HocLai.append((ma,name,d1,d2,d3,dtb))
        cnt+=1

print("Danh sach sinh vien hoc lai")
for i in HocLai:
    print("{} {} {:.2f} {:.2f} {:.2f} {:.2f}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
print("Danh sach nay co {} sinh vien phai hoc lai".format(cnt))
