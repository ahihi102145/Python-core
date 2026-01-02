n=int(input())
max_money = -1
found = False
res = None
for i in range(n):
    a=input().split()
    ten=a[0]
    ma=a[1]
    start=int(a[2])
    end=int(a[3])
    consume = end - start
    money =0
    
    if ma[0] == 'K':
        price = 1070
        money = consume*price
        
        if not found or money > max_money:
            found =True
            max_money= money
            res = (ten,ma,start,end,consume,money)
if not found:
    print("Khong co khach hang la ho kinh doanh.")
else:
    print(*res)           
        