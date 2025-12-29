def tim_phan_tu(a, lst):
    for i in range(len(lst)):
        if lst[i] == a:
            return i
    return 0


a = int(input())

lst=list(map(int,input().strip("[]").split(", ")))
print(tim_phan_tu(a,lst))
