from functools import  cmp_to_key
def cmp (x,y):
    if x+ y > y+ x:
        return -1
    elif x + y < y+ x:
        return 1
    else:
        return 0

n=int(input())
a=list(input().split())
a.sort(key=cmp_to_key(cmp))
res=''.join(a)
print(res)