n=int(input())
order=[]
cnt=0
for i in range(n):
    a=input().split()
    ma=int(a[0])
    ten=a[1]
    sl=int(a[2])
    price=int(a[3])
    revenue=sl*price
    if sl >0:
        order.append((ma,ten,revenue))
        cnt+=1
order.sort(key=lambda x:x[2],reverse=True)
print("Danh sach don hang hop le:",cnt)
for i in order:
    print("{} {} {}".format(i[0],i[1],i[2]))