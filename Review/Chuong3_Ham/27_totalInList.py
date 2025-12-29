lst = list(map(int,input().split(",")))
total=0
for x in lst:
    if x % 2 == 0:
        total += x
print(total)