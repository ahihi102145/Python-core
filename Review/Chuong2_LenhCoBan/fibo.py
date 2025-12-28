
#
# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=' ')
#         a,b=b,a+b
#     print()
# n = int(input())
# fibo(n)
x,d,m=map(int,input().split())
if m%(x*d)==0:
    print(int(m/(x*d)))
else:
    print('-1')