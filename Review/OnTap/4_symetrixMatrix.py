n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
check=1
for i in range(n):
    for j in range(i+1,n):
        if a[i][j] != a[j][i]:
            check=0
            break
    if not check:
        break
if check:
    print("Yes")
else:
    print("No")
