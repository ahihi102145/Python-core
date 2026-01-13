n=int(input())
res=None
minSalary = 1e18

for i in range(n):
    a=input().split()
    ma=int(a[0])
    ten=a[1]
    hsl=float(a[2])
    pc=int(a[3])

    luong = hsl * 2000000 + pc

    if luong < minSalary:
        minSalary=luong
        res=(ma,ten,hsl,pc,luong)
print("Nhan vien co luong thap nhat")
print("{} {} {:.2f} {} {:.2f}".format(*res))


