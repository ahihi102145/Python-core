def cntChan(n):
    cnt = 0
    while n>0:
        d = n%10
        if d%2==0:
            cnt += 1
        n//=10
    return cnt
n=int(input())
a=list(map(int,input().split()))
res=-1
maxVal=0
for i in range(n):
    chan=cntChan(a[i])
    #print(chan)
    if chan>maxVal:
        maxVal=chan
        res=a[i]
print(res)