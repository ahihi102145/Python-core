def ve_hinh_vuong_rong(h):
    n=abs(h)
    print("*"*n)
    for _ in range(n-2):
        print("*" + " "*(n-2)+"*")
    if n>1:
        print("*"*n)

x, y, z = map(int, input().split())

print(x,end="\n")
ve_hinh_vuong_rong(x)
print(y,end="\n")    
ve_hinh_vuong_rong(y)
print(z,end="\n") 
ve_hinh_vuong_rong(z)