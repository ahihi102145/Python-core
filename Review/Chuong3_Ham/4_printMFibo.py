def fibo(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input())
for i in range(1,n+1):
    print(fibo(i),end=' ')