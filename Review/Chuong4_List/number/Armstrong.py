n=int(input())
temp=n
total=0
while temp>0:
    total+=(temp%10)**3
    temp//=10
if total==n:
    print("YES ")
else:
    print("NO")