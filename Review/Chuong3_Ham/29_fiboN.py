def fiboN(n):
    if n<0:
        return 0
    if n==1 :
        return 1
    if n==2:
        return 1
    else:
        return fiboN(n-1)+fiboN(n-2)

n=int(input())
print(fiboN(n))