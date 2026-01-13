def pl(n,a):
    for i in range(1,n):
        if a[i] < a[i-1]:
            print("KHONG_TANG")
            return
    print("TANG")
n=int(input())
a=list(map(float,input().split()))
m=int(input())
b=list(map(float,input().split()))
pl(n,a)
pl(m,b)