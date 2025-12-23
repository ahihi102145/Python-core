"""
Viết chương trình nhập vào một mảng các số nguyên. Sắp xếp mảng đó tăng dần.

Input: 

+ Dòng thứ nhất nhập vào số nguyên N, 1 <= N <= 1000

+ Dòng thứ hai nhập vào N số nguyên cách nhau dấu cách.

Output: 

+ Dòng thứ nhất in ra số phần tử của mảng (N)

+ Dòng thứ hai in ra các phần tử của mảng (đã được sắp xếp tăng dần) cách nhau dấu cách.

Constrains: 

+ Các phần tử trong mảng là các số nguyên


For example:

Input	Result
11
169 224 228 108 212 214 205 145 77 211 241 
11
77 108 145 169 205 211 212 214 224 228 241 
"""
n=int(input())
a= list(map(int,input().split()))
for i in range(n-1):
	for j in range(i+1,n):
		if a[i] > a[j]:
			tg = a[i]
			a[i] = a[j]
			a[j] = tg
for x in a:
	print(x,end="")
#print(*a)