import  math
def check(xa,ya,xb,yb,r):
    d=math.sqrt((xa-xb)**2+(ya-yb)**2)
    if d<r:
        return "trong"
    elif d>r:
        return "ngoai"
    else:
        return "tren"
n=int(input())
cricle=[]
for i in range(n):
    a=input().split()
    ma=int(a[0])
    x=int(a[1])
    y=int(a[2])
    r=float(input())
    cricle.append((x,y,r))

xa, ya, xb, yb = map(int,input().split())
for x,y,r in cricle:
    resA=check(xa,ya,x,y,r)
    print("Diem ({}, {}) nam {} hinh tron tam ({}, {}) ban kinh {:.3f}".format(xa,ya,resA,x,y,r))
    resAb= check(xb, yb, x, y, r)
    print("Diem ({}, {}) nam {} hinh tron tam ({}, {}) ban kinh {:.3f}".format(xb, yb,resAb, x, y, r))

