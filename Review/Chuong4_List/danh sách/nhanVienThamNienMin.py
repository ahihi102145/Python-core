n=int(input())
res=None
minVal = 1e9
for i in range(n):
    a=input().split()
    ma=int(a[0])
    hodem=a[1]
    ten =a[2]
    hsl=float(a[3])
    thamnien=int(a[4])
    if thamnien<minVal:
        minVal=thamnien
        res= (ma,hodem,ten,hsl,minVal)
print("{} {} {} {:.2f} {}".format(*res))