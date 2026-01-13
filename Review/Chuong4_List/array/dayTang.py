def daytang(a,n):
    for i in range(1,n):
        if a[i] <= a[i-1]:
            return "NO"
            break
    return "YES"
n=int(input())
a=list(map(int,input().split()))
print(daytang(a,n))