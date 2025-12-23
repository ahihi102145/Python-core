rows= int(input("Nhap so hang:"))
col = int(input("Nhap so cot:"))
matrix = []
for i  in range(rows):
    row=[]
    for j in range(col):
        print(f"a[ {i} ][ {j} ]=",end=" ")
        row.append(int(input()))
    matrix.append(row)
print("Ma tran vua nhap la:")
for i in range(rows):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()