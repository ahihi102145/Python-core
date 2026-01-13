def sumMatrix(a,b):
    m=len(a)
    n=len(a[0])
    c=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(a[i][j]+b[i][j])
        c.append(row)
    return c

n1,m1=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n1)]
n2,m2=map(int,input().split())
b=[list(map(int,input().split())) for i in range(n2)]
if n1 != n2 or m1 != m2:
    print("Du lieu vao sai")
else:
    c=sumMatrix(a,b)
    print("Ma tran tong")
    for row in c:
        print(*row)

