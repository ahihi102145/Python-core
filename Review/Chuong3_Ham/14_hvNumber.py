def ve_hinh_vuong(n):
    for i in range(n):
        for j in range(n):
            print(i + j + 1, end=" ")
        print()

t = int(input())

for test in range(t):
    n = int(input())
    ve_hinh_vuong(n)
    if test != t - 1:
        print()
