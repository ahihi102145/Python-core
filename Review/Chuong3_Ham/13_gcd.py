import math

x,y,z= map(int,input().split())
if x<=0 or y<=0 or z<=0:
    print("Dữ liệu sai")
else:
    print(math.gcd(x,math.gcd(y,z)))
