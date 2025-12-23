# def perfect_square1(num):
#     if num<0:
#         return 0
#     for i in range(1,int(num**0.5)+1):
#         if i*i==num:
#             return i
#     return 0
from cmath import sqrt


def perfect_square1(num):
    if num <0:
        return 0
    for i in range (1,int(num**0.5)+1):
        if i*i==num:
            return i
    return 0
a,b = map(int, input().split())
cnt =0
start = min(a,b)
end = max(a,b)
for i in range(start,end+1):
    if perfect_square1(i):
        #print(i)
        cnt += 1
print(cnt)
