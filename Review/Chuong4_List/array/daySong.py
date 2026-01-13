n = int(input())
a = list(map(int, input().split()))
if n < 2:
    print("NO")
    exit()
else:
    check =1
    for i in range(1,n-1):
        if not ((a[i] > a[i-1] and a[i] > a[i+1]) or
                (a[i] <a[i-1] and a[i] < a[i+1])) :
            check = 0
            break
    print("YES" if check else "NO")