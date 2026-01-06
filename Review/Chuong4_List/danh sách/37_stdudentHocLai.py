n=int(input().split())
idx=-1
min_st = -1
check =0
HocLai = None
for i in range(n):
    a=input().split()
    name = a[0]
    ma = int(a[1])
    dtoan = float(a[2])
    dttriet = float(a[3])
    dltc = float(a[4])
    dtb = (dttriet+dtoan+dltc)/3

    if dtoan < 4.0:
        check+=1
    if dttriet < 4.0:
        check+=1
    if dltc<4.0:
        check+=1
