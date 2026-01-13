n=int(input())
tong = {}
thu_tu =[]
for i in range(n):
    maSP,maKho,sl=input().split()
    sl=int(sl)

    if maSP not in tong:
        tong[maSP]=sl
        thu_tu.append(maSP)
    else:
        tong[maSP] += sl
maxSP = thu_tu[0]
maxVal=tong[maxSP]
for maSP in thu_tu:
    if tong[maSP]>maxVal:
        maxVal=tong[maSP]
        maxSP=maSP
print(maxSP,maxVal)