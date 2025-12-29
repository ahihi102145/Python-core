def maxInDigit(n):
    if n<0:
        return "Error"
    res = -1e9
    while n>0:
        if res < n%10:
            res = n%10
        n//=10
    return res

x,y,z=map(int,input().split())
print(maxInDigit(x),maxInDigit(y),maxInDigit(z),end=' ')

