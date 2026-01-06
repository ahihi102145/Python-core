n=int(input())
max_sv = -1
Thu_Khoa = None
idx=-1

for i in range(n):
    info = input().split()
    ten = info[0]
    sbd = int(info[1])
    d1= float(info[2])
    d2= float(info[3])
    d3= float(info[4])
    sum_score = d1+d2+d3
    if sum_score>=15.00 and d1>=1.00 and d2>=1.00 and d3>=1.00:
        if sum_score >max_sv:
            max_sv=sum_score
            idx=i
            Thu_Khoa = (sbd,ten,d1,d2,d3,sum_score)
if Thu_Khoa is None:
     print("Khong co thi sinh thi do")
else:
    print("So thu tu cua thu khoa: " + str(idx))
    print("{} {} {:.2f} {:.2f} {:.2f} {:.2f}".format(*Thu_Khoa))


n = int(input())

max_tong = -1
thu_khoa = None
vi_tri = -1

for i in range(n):
    a = input().split()
    ten = a[0]
    sbd = int(a[1])
    d1 = float(a[2])
    d2 = float(a[3])
    d3 = float(a[4])

    tong = d1 + d2 + d3

    if tong >= 15.0 and d1 >= 1.0 and d2 >= 1.0 and d3 >= 1.0:
        if tong > max_tong:
            max_tong = tong
            thu_khoa = (sbd, ten, d1, d2, d3, tong)
            vi_tri = i

if thu_khoa is None:
    print("Khong co thi sinh thi do")
else:
    print("So thu tu cua thu khoa: " + str(vi_tri))
    print(str(thu_khoa[0]) + " " + thu_khoa[1] + " " +
          "{:.2f}".format(thu_khoa[2]) + " " +
          "{:.2f}".format(thu_khoa[3]) + " " +
          "{:.2f}".format(thu_khoa[4]) + " " +
          "{:.2f}".format(thu_khoa[5]))
