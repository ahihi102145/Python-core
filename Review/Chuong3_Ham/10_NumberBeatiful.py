def snt(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

def fibo(n):
    a,b=0,1
    while b<n:
        a,b=b,a+b
    return b==n or n==0

def soDep(n):
    if not snt(n):
        return 0
    total=0
    while n>0:
        total+=n%10
        n//=10
    return fibo(total)

a,b=map(int,input().split())
res=[]
for i in range(a,b+1):
    if soDep(i):
        res.append(i)
if not res:
    print("-1")
else:
    print(*res)