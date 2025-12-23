import math


def ptb1(a,b):
    if a==0:
        if b==0:
            print("VSN")
        else:
            print("VN")
    else:
        print("{:.3f}".format(-b/a))

def ptb2(a,b,c):
    x1=0
    x2=0
    if a==0:
        ptb1(b,c)
    else:
        delta= b*b - 4*a*c
        if delta<0:
            print("VN")
        elif delta==0:
            x1=x2=-b/2*a
            print("{:.2f}".format(x1))
        else:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            res1=min(x1,x2)
            res2=max(x1,x2)
            print("{:.3f} {:.3f}".format(res1,res2))

a,b,c=map(float,input().split())
ptb2(a,b,c)