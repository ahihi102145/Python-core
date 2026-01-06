n=int(input())
max_money = -1
customer = None
idx = -1

for i in range(n):
    info = input().split()
    ten = info[0]
    ma = int(info[1])
    start = int(info[2])
    end = int(info[3])
    consume = end-start 
    money =0

    if consume <=100:
        money= consume*1000
    elif consume <=200:
        money = 100*1000 + (consume-100)*1500
    else:
        money = 100*1000 + 100*1500 + (consume-200)*2000
    if money > max_money:
        max_money = money
        customer = (ma,ten,start,end,consume,max_money)
        idx = i
print("Khach hang phai tra tien nhieu nhat: {}".format(idx))
print("{} {} {} {} {} {}".format(*customer))

    
n = int(input())

max_tien = -1
kh_max = None
vi_tri = -1

for i in range(n):
    a = input().split()
    ten = a[0]
    ma = a[1]
    dau = int(a[2])
    cuoi = int(a[3])

    tieu_thu = cuoi - dau
    tien = 0

    if tieu_thu <= 100:
        tien = tieu_thu * 1000
    elif tieu_thu <= 200:
        tien = 100 * 1000 + (tieu_thu - 100) * 1500
    else:
        tien = 100 * 1000 + 100 * 1500 + (tieu_thu - 200) * 2000

    if tien > max_tien:
        max_tien = tien
        kh_max = (ma, ten, dau, cuoi, tieu_thu, tien)
        vi_tri = i

print("Khach hang phai tra tien nhieu nhat: " + str(vi_tri))
print(kh_max[0] + " " + kh_max[1] + " " +
      str(kh_max[2]) + " " + str(kh_max[3]) + " " +
      str(kh_max[4]) + " " + str(kh_max[5]))

