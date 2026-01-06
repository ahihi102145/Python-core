def phan_loai(a,n):
    chan=[x for x in a if x%2==0]
    le=[x for x in a if x%2!=0]
    if chan:
        print(" ".join(map(str,chan)))
    else:
        print("Khong co so chan")
    if le:
        print(" ".join(map(str,le)))
    else:
        print("Khong co so le")
n = int(input())
lst = list(map(int, input().split()))


phan_loai(lst,n)
