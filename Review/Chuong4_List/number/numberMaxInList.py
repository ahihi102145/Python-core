def total(n):
    total = 0
    while n > 0:
        total += n%10
        n//=10
    return total
n=int(input())
a=list(map(int,input().split()))
maxNum=-1
res=None
for i in range(n):
    s=total(a[i])
    if s>maxNum:
        maxNum=s
        res=a[i]
print(res)