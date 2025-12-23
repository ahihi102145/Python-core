""""
Viết chương trình nhập vào 2 ma trận X (có n1 hàng, m1 cột) và Y (có n2 hàng, m2 cột) các số nguyên. Tính tổng 2 ma trận đó và in kết quả ra màn hình. Nếu không tính được tổng 2 ma trận thì in ra thông báo "Du lieu vao sai"

Input: 

+ Dòng thứ nhất nhập vào n1 và m1 là số hàng và số cột của ma trận X. 

+ Dòng tiếp theo nhập vào các phần tử của ma trận X gồm n1 hàng, m1 cột

+ Dòng tiếp theo nhập vào n2 và m2 là số hàng và số cột của ma trận Y. 

+ Dòng tiếp theo nhập vào các phần tử của ma trận Y gồm n2 hàng, m2 cột

Output:

+ Nếu tính được tổng:

- Dòng thứ nhất in ra thông báo "Ma tran tong"

- Dòng thứ hai in ra số hàng và số cột cách nhau dấu cách

- Các dòng tiếp theo in ra các phần tử của ma trận cách nhau dấu cách.

+ Nếu không tính được tổng:

- In ra thông báo "Du lieu vao sai"

Constranins: 1<=n, m<=100, các phần tử trong ma trận là các số nguyên.


For example:

Input	Result
10 13
17 24 10 19 3 11 22 8 23 14 16 11 3 
18 22 19 12 7 12 9 23 16 4 3 16 10 
15 17 13 6 15 17 14 23 21 5 15 4 20 
0 6 1 18 23 4 23 9 4 6 15 16 1 
6 8 19 14 1 23 12 13 18 7 4 16 8 
15 14 8 4 5 2 6 23 11 21 20 24 22 
20 4 2 23 22 12 11 15 11 11 5 17 5 
24 6 2 0 0 16 24 16 5 7 16 7 12 
7 12 3 8 20 9 9 8 21 13 22 21 6 
5 13 18 0 16 12 5 10 9 24 12 23 8 
10 13
20 16 2 0 16 11 24 20 21 21 23 24 18 
9 6 9 3 24 18 13 0 13 2 17 3 18 
23 8 7 21 10 17 13 14 9 16 10 1 0 
24 19 6 23 3 24 8 19 9 14 2 20 10 
18 18 23 12 14 3 23 0 8 18 5 21 23 
6 14 23 9 7 22 22 13 17 13 4 15 7 
8 16 15 13 6 11 2 9 22 5 3 21 12 
11 0 8 19 17 19 16 6 23 22 1 21 24 
7 1 17 14 0 12 0 10 3 19 11 13 1 
14 5 23 2 10 7 10 13 1 17 7 7 7 
Ma tran tong
37 40 12 19 19 22 46 28 44 35 39 35 21  
27 28 28 15 31 30 22 23 29 6 20 19 28 
38 25 20 27 25 34 27 37 30 21 25 5 20 
24 25 7 41 26 28 31 28 13 20 17 36 11 
24 26 42 26 15 26 35 13 26 25 9 37 31 
21 28 31 13 12 24 28 36 28 34 24 39 29 
28 20 17 36 28 23 13 24 33 16 8 38 17 
35 6 10 19 17 35 40 22 28 29 17 28 36 
14 13 20 22 20 21 9 18 24 32 33 34 7 
19 18 41 2 26 19 15 23 10 41 19 30 15 
"""

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



A, m1, n1 = nhapmatran()


B, m2, n2 = nhapmatran()

if m1 != m2 or n1 != n2:
    print("Du lieu vao sai")
else:
    C = sumtwomatrix(A, B)
    print("Ma tran tong")
    for row in C:
        print(*row)