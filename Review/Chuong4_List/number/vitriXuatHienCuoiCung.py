n = int(input())

if n == 0:
    print(-1)
else:
    a = list(map(int, input().split()))
    k = int(input())

    idx = -1
    for i in range(n - 1, -1, -1):
        if a[i] == k:
            idx = i
            break

    print(idx)
