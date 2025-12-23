def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
def snt(n):
    if n <=2:
        return 0
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
a,b = map(int, input().split())

for i in range(a,b+1):
    if fibo(sum(i)) and snt(i):
        print(i)
    else:
        print(-1)