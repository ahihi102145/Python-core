def draw_square(n):
    for i in range(n):
        stat = i +1
        for j in range(stat,stat+n):
            print(j,end=" ")
        print()

T = int(input())
for _ in range(T):
    n = int(input())
    draw_square(n)
    print()