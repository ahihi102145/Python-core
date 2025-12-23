def ucln(a,b):
    while(b!=0):
        a,b = b, a%b
    return a    
a,b=map(int,input().split())
print("UCLN của {} và {} là: {}".format(a, b, ucln(a, b)))