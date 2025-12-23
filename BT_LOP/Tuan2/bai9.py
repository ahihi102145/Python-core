def ucln(a,b):
    while(b!=0):
        a,b = b,a%b
    return a
def bcnn(a,b):
    return a*b//ucln(a,b)

a,b=map(int,input().split())
print("BCNN của {} và {} là: {}".format(a, b, bcnn(a, b)))    