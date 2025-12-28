def convertDecimalToBinary(n):
    if n==0:
        return "0"
    lst=[]
    while n>0:
        lst.append(n % 2)
        n = n // 2
    lst.reverse()
    return ''.join(map(str,lst))

s=input()
arr=list(map(int,s.split(',')))
# arr = list(map(int, input().split(',')))
# res=[convertDecimalToBinary(i) for i in arr]
# print(','.join(res))
print(','.join(convertDecimalToBinary(i) for i in arr))
