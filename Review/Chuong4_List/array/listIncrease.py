from functools import  cmp_to_key
def cmp(a,b):
    if a + b < b+ a :
        return 1
    elif a + b > b+ a:
        return -1
    else:
        return 0
n=int(input())
a=input().split()
a.sort(key=cmp_to_key(cmp))
result = ''.join(a)
print(result)