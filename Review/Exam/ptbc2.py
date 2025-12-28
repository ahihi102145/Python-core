import math
def ptb1(a,b):
    if a==0:
        if b==0:
            print ("VSN")
        else:
            print ("VN")
    else:
        x=-b/a
        print ("{:.3f}".format(x))
    
def ptb2(a,b,c):
    if a==0:
        return ptb1(b,c)
    else:
        d=b**2-4*a*c
        if d<0:
            print ("VN")
        elif d==0:
            x=-b/(2*a)
            print ("{:.3f}".format(x))
        else:
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            print ("{:.3f}".format(min(x1,x2)), "{:.3f}".format(max(x1,x2)))

a,b,c=map(float,input().split())
ptb2(a,b,c)