import math
a,b,c=map(float,input().split())
if a >0 and b>0 and c>0 and a+b >c and b+c >a and c+a >b:
    cv=a+b+c
    p=(a+b+c)/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac: {:.2f}".format(dt))
    print("Chu vi tam giac: {:.2f}".format(cv))
else:
    print("DL sai")