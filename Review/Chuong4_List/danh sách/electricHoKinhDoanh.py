n=int(input())
res=None
maxVal=-1
for i in range(n):
    a=input().split()
    ten=a[0]
    ma=a[1]
    start = int(a[2])
    end = int(a[3])
    consume = end-start
    if ma[0]=='K':
        price = consume*1070
        if price>maxVal:
            maxVal=price
            res=(ten,ma,start,end,consume,price)
if res is None:
    print("Khong co khach hang la ho kinh doanh.")
else:
    print(*res)
