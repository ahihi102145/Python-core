# dung so hoc
# n=int(input())
# tmp=n
# cnt=0
# t=n
# while t>0:
#     cnt=cnt+1
#     t//=10
#
# s=0
# t=n
# while t>0:
#     digit=t%10
#     s += digit**cnt
#     t//=10
#
# if s==tmp:
#     print(1)
# else:
#     print(0)

#dung string
n=(input())
k=len(n)
s =sum(int(d)**k for d in n)
if  s==int(n):
    print(1)
else:
    print(0)
