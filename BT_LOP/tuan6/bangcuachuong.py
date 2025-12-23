# a,b= map(int,input().split())
# for i in range(a,b+1):
#     for j in range(1,10):
#         if i<=j:
#             print("{}x{}={}".format(i,j,i*j))

 

a1,b1,c1= map(float,input().split())
a2,b2,c2= map(float,input().split())

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