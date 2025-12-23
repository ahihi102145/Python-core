n= int(input())
lst = []
for _ in range(n):
    info = input().split()
    ten = info[0]
    ma = int(info[1])
    hsl = float(info[2])
    pc = int(info[3])
    luong = hsl * 2000000 + pc
    lst.append((ma,ten,hsl,pc,luong))
lst.sort(key=lambda x:x[4], reverse=True)
print("Danh sach nhan vien da sap xep: {}".format(n))
for i in lst :
    print("{} {} {:.2f} {} {:.2f}".format(i[0],i[1],i[2],i[3],i[4]))

n=int(input())
lst =[]
for _ in range(n):
    info = input().split()
    ten = info[0]
    ma= info[1]
    hsl = float(info[2])
    pc = int(info[3])
    luong = hsl * 2000000 + pc
    lst.append(( ma,ten, hsl, pc, luong))
lst.sort(key=lambda x: x[4],reverse=True)
print("Danh sach nhan vien da sap xep: {}".format(n))
for staff in lst:
    print("{} {} {:.2f} {} {:.2f}".format(staff[0], staff[1], staff[2], staff[3], staff[4]))
