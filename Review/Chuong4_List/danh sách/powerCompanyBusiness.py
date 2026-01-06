n=int(input())
check = False
max_money = -1
res = None
for i in range(n):
    infor = input().split()
    ten=infor[0]
    ma= infor[1]
    start = int(infor[2])
    end = int(infor[3])
    consume = end - start

    if ma[0] == 'D':
        price = 1050
        momey = consume*price

        if not check or momey > max_money:
            check = True
            max_money = momey
            res = (ma,ten,start,end,consume,momey)
if not check:
    print("Khong co khach hang la doanh nghiep.")
else:
    print("{} {} {} {} {} {}".format(res[0],res[1],res[2],res[3],res[4],res[5]))