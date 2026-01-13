n=int(input())
drl={
 "hd1": 5,
    "hd2": 8,
    "hd3": 10,
    "hd4": 10,
    "hd5": 15
}
tong={}
tensv={}
thutu=[]
for i in range(n):
    masv,ten,hd=input().split()
    if masv not in tong:
        tong[masv]=0
        tensv[masv]=ten
        thutu.append(masv)
    tong[masv]+=drl[hd]

res=0
for masv in thutu:
    if tong[masv] <=70:
        print(masv,tensv[masv],tong[masv])
        res=1
if res==0:
    print("Khong co sinh vien nao diem ren luyen < 70")