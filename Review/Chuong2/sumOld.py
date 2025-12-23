
a,b= map(int,input().split())
x=min(a,b)
y=max(a,b)
total =0
cnt=0
for i in range(x,y+1):
    if i%2==0:
        total += i
        cnt+=1

print(total)