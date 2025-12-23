# def nhapmatran(n):
#     a=[]
#     for i in range(n):
#         dong = list(map(int,input().split()))
#         a.append(dong)
#     return a

# n=int(input())
# min_value = -1e9
# matrix = nhapmatran(n)
# for i in range(n):
#     if matrix[i][i] > min_value:
#         min_value = matrix[i][i]
# print(min_value)

""""
Nhập ma trận vuông a có kích thước nxn.

Tìm và in ra giá trị lớn nhất trên đường chéo chính của ma trận.

Input Format

Dữ liệu nhập vào trên n+1 dòng.

Dòng 1: kích thước (số hàng=số cột) ma trận vuông - n.
n dòng còn lại: các dòng của ma trận, mỗi dòng chứa các a[i][j] cách nhau 1 dấu cách.
Constraints

n, a[i][j]: số nguyên
1 <= n <= 100
Output Format

In ra giá trị lớn nhất trên đường chéo chính.

For example:

Input	Result
2
-12 -47
28 33
33
3
37 38 -9
-23 19 -17
7 38 -18
37
"""

def nhapmatran(n):
    a=[]
    for i in range(n):
        dong =list(map(int,input().split()))
        a.append(dong)
    return a
    
n=int(input())
matrix=nhapmatran(n)

min_value=-1e9
for i in range(n):
    if matrix[i][i] > min_value:
        min_value = matrix[i][i]
print(min_value)

