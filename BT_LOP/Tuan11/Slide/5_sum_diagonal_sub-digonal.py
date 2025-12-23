
n = int(input())
m = int(input())
a=[]
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

sum_main=0
sum_sub=0
for i in range(n):
    sum_main += a[i][i]
    sum_sub += a[i][n-i-1]
print(sum_main)
print(sum_sub)
