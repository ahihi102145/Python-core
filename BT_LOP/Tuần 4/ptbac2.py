import math

a,b,c = map(float,input().split())
if a==0:
    if b == 0:
        if c == 0:
            print("VSN")
        else:
            print("VN")
    else:
        print("{:.3f}".format(-c/b))
else:
    x1=x2=0
    delta = (b*b - 4*a*c)
    if delta < 0:
        print("VN")
    elif delta == 0:
        x1=x2=-b/(2*a)
        print("{:.3f}".format(x1))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        if x1 < x2:
            print("{:.3f} {:.3f}".format(x1,x2))
        else:
            print("{:.3f} {:.3f}".format(x2, x1))