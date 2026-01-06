<<<<<<< HEAD
def hoanhao(n):
    total=1
    i=2
    while i*i<=n:
        if n%i==0:
            total=total+i*i
=======
n=int(input())
max_money = -1
idx = -1
res = None

for i in range(n):
    a=input().split()
    ten=a[0]
    ma=int(a[1])
    start=int(a[2])
    end=int(a[3])
    consume = end - start
    price =0
    if consume <100:
        price = consume *1000
    elif 100 < consume < 200:
        price = 100*1000 + (consume-100)*1500
    else:
        price = 100*1000 + 100*1500 + (consume-200)*2000
    if price >max_money :
        max_money=price
        idx=i
        res=(ma,ten,start,end,consume,price)
        
print("Khach hang phai tra tien nhieu nhat: {}".format(idx))
print("{} {} {} {} {} {}".format(*res))
>>>>>>> f1307ffbb4b7119c73f15728c57e73b56cc17a2e
