n=int(input())
a=list(map(int,input().split()))
tong =0
dep = True
for i in a:
    if i <= tong:
        dep = False
        break
    tong+=i

if dep:
    print("YES")
else:
    print("NO")
