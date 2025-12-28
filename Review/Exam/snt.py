import math

def snt(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

a, b = map(int, input().split())

start, end = min(a, b), max(a, b)
lst = []

for i in range(start, end + 1):
    if snt(i):
        lst.append(i)

if not lst:
    print("Khong co")
else:
    if a > b:
        lst.sort(reverse=True)   
    else:
        lst.sort()               
    print(*lst)
'''
Viết chương trình nhập vào 2 số nguyên a, b. In ra các số nguyên tố trong đoạn [a, b] hoặc [b, a]. Nếu trong đoạn này không có số nguyên tố thì in ra thông báo "Khong co". Biết số nguyên tố là số nguyên dương >=2 và chỉ chia hết cho 1 và chính nó.

Input: a, b là số nguyên cách nhau dấu cách.

Output: các số nguyên tố tìm được viết trên một dòng, cách nhau dấu cách. Hoặc thông báo "Khong co".

Constrains: các số kiểu int 

Ví dụ 1: 

+ Input

a= -30, b=-9  

+ Output

Khong co

Ví dụ 2: 

+ Input

a= 0, b=9  

+ Output

2 3 5 7

Ví dụ 2: 

+ Input

a= 9, b=0  

+ Output

7 5 3 2




For example:

Input	Result
-9 -33
Khong co
28 18
23 19
'''