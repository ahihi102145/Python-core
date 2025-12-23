
d= a1*b2-a2*b1
dx= c1*b2-c2*b1
dy= a1*c2-a2*c1
if d==0:
    if dx==0 and dy==0:
        print("VN")
    else:
        print("VSN")
else:
    x= d/dx
    y= d/dy
    print("{:.5f} {:.5f}".format(x,y)) 