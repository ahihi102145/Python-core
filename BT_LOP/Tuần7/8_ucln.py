def ucln(a,b):
    while b!=0:
        a,b=b,a%b
    return a

a,b,c = map(int,input().split())
if a<0 or b<0 or c<0:
    print("Dữ liệu sai")
else:
    print(ucln(ucln(a,b),c))