def check(a,n):
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            return 0
    return 1
n=int(input())
a=list(map(float,input().split()))
m=int(input())
b=list(map(float,input().split()))

if check(a,n) == 1:
    print("TANG")
else:
    print("KHONG_TANG")

if check(b,m) == 1:
    print("TANG")
else:
    print("KHONG_TANG")



def la_day_tang(a, n):
    for i in range(1, n):
        if a[i] <= a[i - 1]:
            return 0
    return 1

n = int(input())
a = list(map(float, input().split()))


m = int(input())
b = list(map(float, input().split()))

if la_day_tang(a, n) == 1:
    print("TANG")
else:
    print("KHONG_TANG")

if la_day_tang(b, m) == 1:
    print("TANG")
else:
    print("KHONG_TANG")
