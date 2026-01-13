def ve_tam_giac_can(h):
    n=abs(h)
    if h>0:
        for i in range(1,n+1):
            print(" "*(n-i)+"*"*(2*i-1))
    else:
        for i in range(n,0,-1):
            print(" "*(n-i)+"*"*(2*i-1))

x, y, z = map(int, input().split())
print(x,end="\n")
ve_tam_giac_can(x)
print(y,end="\n")
ve_tam_giac_can(y)
print(z,end="\n")
ve_tam_giac_can(z)
# def draw(n):
#     for i in range(1,n+1):
#         print(" "*(n-i)+ "* "*i)
#     print()
# n=int(input())
# draw(n)