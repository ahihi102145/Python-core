def nhapmatran():
	n,m=map(int,input().split())
	a=[]
	for _ in range(m):
		row=list(map(int,input().split()))
		a.append(row)
		return a,n,m
		
def sumTowMatrix(a,b):
	m=len(a)
	n=len(a[0])
	c=[]
	for i in range(m):
		row=[]
		for j in range(n):
			row.append(a[i][j]+b[i][j])
		c.append(row)
	return c
	
a,m1,n1 = nhapmatran()
b,m2,n2 = nhapmatran()

if m1 !=m2 or n1 !=n2:
	print("Du lieu vao sai")
else:
	c= sumTowMatrix(a,b)
	print("Ma tran tong")
	for row in c:
		print(*row)
	