n=int(input())
m=int(input())
a=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in range(n):
    for j in range(m):
        if a[i][j] < 0:
            cnt+=1
print(cnt)