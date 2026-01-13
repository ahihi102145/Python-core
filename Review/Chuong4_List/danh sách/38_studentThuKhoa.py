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

