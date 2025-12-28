n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=lst[i]
print(sum)
