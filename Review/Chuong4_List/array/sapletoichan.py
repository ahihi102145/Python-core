n=int(input())
a=list(map(int,input().split()))
# res=[]
# for i in range(n):
#     if a[i]%2!=0:
#         res.append(a[i])
# for i in range(n):
#     if a[i]%2==0:
#         res.append(a[i])
# print(*res)
check=1
for i in range(1,n):
    if a[i] <=a[i-1]:
        check=0
        break
if check==0:
    print("NO")
else:
    print("YES")