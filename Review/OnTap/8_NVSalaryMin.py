n=int(input())
res=None
minVal=1e9
for _ in range(n):
    a=input().split()
    ho=a[0]
    ten=a[1]
    hsl=float(a[2])
    pc=int(a[3])
    luong=hsl*2000000+pc
    if luong<minVal:
        minVal=luong
        res=(ho, ten, hsl, pc, minVal)
print(*res)
