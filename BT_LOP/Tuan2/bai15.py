import math
def snt(n):
    if n<=1:
        return False
    check = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            check=False
            break
    return check
n = int(input())
if snt(n)==True:
    print("{} la SNT".format(n))  
else:
    print("{} khong la SNT".format(n)) 
