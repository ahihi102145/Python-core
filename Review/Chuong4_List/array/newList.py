n=int(input())
a=list(map(int,input().split()))
newList=[]
total=0
for i in range(n):
    total += a[i]
    newList.append(total)
print(*newList)
