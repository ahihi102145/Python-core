n=int(input())
lst=[]
for _ in range(n):
    info = input().split()
    ten=info[0]
    ma=info[1]
    hsl=info[2]
    pc=info[3]
    luong = hsl * 2000000  + pc
    lst.append((ma,ten,hsl,pc,luong))
lst.sort(key=lambda x:x[4],reverse=True)
print("Danh sach nhan vien da sap xep: {}".format(n))
for s in lst:
    print("{} {} {:.2f} {} {:.2f}".format(s[0],s[1],s[2],s[3],s[4]))