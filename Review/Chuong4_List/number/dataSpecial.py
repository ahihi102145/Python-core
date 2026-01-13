d,m= map(int,input().split())
cnt=0
for mm in range(1,m+1):
    for dd in range(1,d+1):
        if dd*mm == dd+mm:
            cnt+=1
print(cnt)