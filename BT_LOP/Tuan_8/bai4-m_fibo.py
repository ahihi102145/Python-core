# def fibo1(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fibo1(n-1)+fibo1(n-2)


def fibo1(n):
    if n==1 or n==2:
        return 1
    return fibo1(n-1)+fibo1(n-2)
n = int (input().strip())
for i in range(1,n+1):
    print(fibo1(i),end=' ')