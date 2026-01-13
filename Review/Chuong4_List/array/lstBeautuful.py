# n=int(input())
# a=list(map(int,input().split()))
# tong =0
# dep = True
# for i in a:
#     if i <= tong:
#         dep = False
#         break
#     tong+=i
#
# if dep:
#     print("YES")
# else:
#     print("NO")



n=int(input())
a=list(map(int,input().split()))
total=0
for i in range(n):
    if i < total :
        print("NO")
        total+=i
print("YES")