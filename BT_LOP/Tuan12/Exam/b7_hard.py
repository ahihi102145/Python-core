n,k= map(int, input().split())
a=list(map(int, input().split()))
fre=[0]*501
cnt=0
for i in range(n):
    res = k - a[i]*a[i]
    if 1 <= res <= 500:
        cnt+=fre[res]
    if a[i] + a[i]*a[i] == k:
        cnt+=1
    fre[a[i]]+=1
print(cnt)