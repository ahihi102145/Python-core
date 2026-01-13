import math
def checkpoint(px,py,cx,cy,r):
    d=math.sqrt((px-cx)**2+(py-cy)**2)
    if abs(d-r) < 1e-6:
        return "tren"
    elif d < r:
        return "trong"
    else:
        return "ngoai"
n=int(input())
res=[]
for i in range(n):
    a=input().split()
    ma=a[0]
    cx=int(a[1])
    cy=int(a[2])
    r=float(a[3])
    res.append((cx,cy,r))
xa,ya,xb,yb=map(int,input().split())
for cx,cy,r in res:
    resA= checkpoint(xa,ya,cx,cy,r)
    print("Diem ({}, {}) nam {} hinh tron tam ({}, {}) ban kinh {:.3f}".format(xa,ya,resA,cx,cy,r))
    resB= checkpoint(xb,yb,cx,cy,r)
    print("Diem ({}, {}) nam {} hinh tron tam ({}, {}) ban kinh {:.3f}".format(xb,yb,resB,cx,cy,r))
