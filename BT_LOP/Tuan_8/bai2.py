def binary(n):
    if n == 0:
        return '0'
    lst = []
    while n>0:
        lst.append(str(n%2))
        n //= 2

    lst.reverse()
    return ''.join(lst)
#
# def binary(n):
#     if n==0:
#         return 0
#     lst =[]
#     while n>0:
#         lst.append(str(n%2))
#         n //= 2
#     lst.reverse()
#     return ''.join(lst)
num = input().strip().split(',')
res = [binary(int(i)) for i in num ]
print(','.join(res))

