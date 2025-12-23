def primary(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
#Đếm tổng số nguyên tố trong khoảng n.
# n = int(input())
# cnt=0
# for i in range(2,n+1):
#     if primary(i):
#         cnt+=1
# print(cnt)

#Cho số X, tìm số nguyên tố lớn nhất nhỏ hơn X.
n = int(input())
for i in range(n-1,1,-1):
    if primary(i) and i<n:
        print(i)
        break