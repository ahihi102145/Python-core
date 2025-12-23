a,b=map(int,input().split())
cnt=0
total=0
start=min(a,b)
end=max(a,b)
for i in range(start,end+1):
    if i%2!=0:
        total+=i
        cnt+=1
print(cnt,total)

