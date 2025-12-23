n=int(input())
a=[]
for i in range(n):
    row = list(map(int,input().split()))
    a.append(row)

min_val= -1e9
for i in range(n):
    if a[i][i] > min_val:
        min_val = a[i][i]
print(min_val)