def checksnt (n):
    if n<1: return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def cnt(a,b):
    dem=0
    if a<1: return 0
    for i in range(a,b+1):
        if(checksnt(i)):
            dem+=1
    return dem
a,b = map(int,input().split())
print(cnt(a,b))

