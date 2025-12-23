import math
def shh(n):
    sum=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sum+=i
        if  i!= n//i:
            sum+=n//i

    if sum==n:
        return "{} la so hoan hao".format(n)
    else :
        return "{} khong la so hoan hao".format(n)
    
n = int(input())
print(shh(n))    