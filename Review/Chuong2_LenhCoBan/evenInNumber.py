def cnt_even(n):
    cntOld=0
    cntEven=0
    while n>0:
        digit=n%10
        if digit%2==0:
            cntEven+=1
        else:
            cntOld+=1
        n=n//10
    return cntEven , cntOld
n=int(input())
even, old=cnt_even(n)
print(old,even)

