msv = int(input("Nhap ma sinh vien:"))
ho ,ten= input("Nhap ho va ten:").split()
d1,d2,d3 = map(int,input("nhap diem 3 diem:").split())
tong = d1+d2+d3


#dung f-string:
print(f"ma sv :{msv:05d}")
print(f"Ho ten :{ho} {ten}")
print(f"diem cac mon :{d1:.2f}, {d2:.2f}, {d3:.2f}")
print(f"diem tong :{tong:.2f}")

#dung format
print("ma sv :{1:05d}".format(msv))
print("Ho ten :{} {}".format(ho, ten))
print("diem cac mon :{:.2f}, {:.2f}, {:.2f}".format(d1,d2,d3))
print("diem tong :{:.2f}".format(tong))