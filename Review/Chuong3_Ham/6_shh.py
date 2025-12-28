# def so_hoan_hao(n):
#     if n<=1:
#         return 0
#     total=1
#     i=2
#     while i*i<=n:
#         if n%i==0:
#             total+=i
#             if i!=n//i:
#                 total+=n//i
#         if total>n:
#             return 0
#         i +=1
#     return total==n

# a, b = map(int, input().split())

# ket_qua = []

# if a <=b:
#     for i in range(a,b+1):
#         if so_hoan_hao(i):
#             ket_qua.append(i)
# else:
#     for i in range(a, b-1, -1):
#         if so_hoan_hao(i):
#             ket_qua.append(i)

# if not ket_qua:
#     print("Khong co")
# else:
#     print(*ket_qua)

def so_hoan_hao(n):
    if n<=1:
        return 0
    total =1
    i=2
    while i*i<=n:
        if n%i==0:
            total+=i
            if i!=n//i:
                total+=n//i
        if total >n:
            return 0
        i+=1
    return total==n
a,b=map(int ,input().split())
res = []
if a<=b:
    for i in range(a,b+1):
        if so_hoan_hao(i):
            res.append(i)
else:
    for i in range(a,b-1,-1):
        if so_hoan_hao(i):
            res.append(i)

if not res:
    print("Khong co")
else:
    print(*res)