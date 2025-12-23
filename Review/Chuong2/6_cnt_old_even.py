def b6(n):
    cntOld=0
    cntEven=0
    while n!=0:
        digit=n%10
        if digit % 2 == 0:
            cntOld += 1
        else:
            cntEven += 1
        n//=10
    return cntEven,cntOld
n=int(input())
print(*b6(n))