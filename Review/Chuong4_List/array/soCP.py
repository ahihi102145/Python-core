import  math
n=int(input())
if n<0:
    print("NO")
temp = int(math.sqrt(n))
if temp*temp == n:
    print("YES")
else:
    print("NO")