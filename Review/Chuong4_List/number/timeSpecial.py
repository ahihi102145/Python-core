hh,mm=input().split()
hh=hh.zfill(2)
mm=mm.zfill(2)
check =1
if not (0 <= int(hh) <= 23 and 0 <= int(mm) <= 59):
    check =0
if (int(hh) + int(mm)) %5!=0:
    check =0
res=hh+mm
if len(res) != len(set(res)):
    check =0

hhNew=mm
mmNew=hh

if not (0 <=int(mmNew) <= 23 and 0 <= int(hhNew) <= 59):
    check =0

if check == 1:
    print("DAC BIET")
else:
    print("KHONG DAC BIET")