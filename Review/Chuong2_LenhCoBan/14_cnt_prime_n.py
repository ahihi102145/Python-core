def prime(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
cnt=0
for i in range(0,n+1):
    if prime(i):
        cnt=cnt+1
print(cnt)