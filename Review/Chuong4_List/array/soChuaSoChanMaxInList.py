def chan(n):
    cnt = 0
    while n != 0:
        ditgit = n % 10
        if ditgit % 2 == 0:
            cnt += 1
        n //= 10
    return cnt


n = int(input())
a = list(map(int, input().split()))
maxEven = 0
res = -2
for i in range(n):
    c = chan(a[i])
    if c > maxEven:
        maxEven = c
        res = a[i]
if maxEven == 0:
    print(-1)
else:
    print(res)
