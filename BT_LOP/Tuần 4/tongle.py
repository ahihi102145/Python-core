def sumOld(a,b):
    sum = 0
    cnt = 0
    for i in range(a,b+1):
        if i%2!=0:
            sum += i
            cnt += 1
    print("{} {}".format(cnt,sum))

a,b = map(int,input().split())
if a<b:
    sumOld(a,b)
else:
    sumOld(b,a)