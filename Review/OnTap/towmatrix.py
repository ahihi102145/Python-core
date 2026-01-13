def nhapmatran():
    n,m= map(int,input().split())
    a= []
    for _ in range(m):
        row= list(map(int,input().split()))
        a.append(row)
        return a,n,m

def sumtwomatrix(A,B):
    m=len(A)
    n=len(A[0])
    c= []
    for i in range(m):
        row= []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        c.append(row)
    return c

n1,m1= map(int,input().split())
A= [list(map(int,input().split())) for i in range(n1)]

n2,m2= map(int,input().split())
B= [list(map(int,input().split())) for i in range(n2)]

if m1 != m2 or n1 != n2:
    print("Du lieu vao sai")
else:
    C = sumtwomatrix(A, B)
    print("Ma tran tong")
    for row in C:
        print(*row)