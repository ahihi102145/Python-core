def increase_series(a,n):
    for i in range(n-1):
        if a[i] >=  a[i+1]:
            return 0
    return 1

n = int(input())
a = list(map(float, input().split()))
if increase_series(a,n) == 1:
    print("TANG")
else:
    print("KHONG_TANG")

m = int(input())
b = list(map(float, input().split()))

if increase_series(b,m) == 1:
    print("TANG")
else:
    print("KHONG_TANG")