# rows = int (input("Row:"))
# column = int (input("Column:"))
# matrix=[]
# #matrix = [list(0 for j in range(column)) for i in range(row)]
# for i in range(rows):
# 	row=[]
# 	for j in range(column):
# 		row.append(int(input()))
# 	matrix.append(row)
# print("\n matrix is:")
# for i in range(rows):
# 	for j in range(column):
# 		print(matrix[i][j],end=" ")
# 	print()
a,b= map(int,input().split())
ds= [list(map(int,input().split())) for i in range(a)]
print("Matrix")
for i in range(a):
	for j in range(b):
		print(ds[i][j],end=" ")
	print()