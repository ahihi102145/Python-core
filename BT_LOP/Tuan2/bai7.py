import math
a,b,c= map(int,input().split())
p=(a+b+c)/2
print("Dien tich tam giac : {:.2f}".format(math.sqrt(p*(p-a)*(p-b)*(p-c))))