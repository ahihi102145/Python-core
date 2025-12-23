# x,d,m = map(int,input().split())
# if m%(x*d) ==0 :
#     print(m//(x*d))
# else:
#     print(-1)    

# def primary(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True


# n= int(input())
# cnt=0
# for i in range(n-1,1,-1):
#     if primary(i) and i<n:
#         print(i)
#         break


# def fibo(n):
#     a,b=0,1
#     for _ in range(n):
#         a,b=b,a+b
#     return a   

# n = int(input())
# for i in range(n):
#     print(fibo(i),end=' ')


# n = int(input())
# cntOld = 0
# cntEven = 0
# if n>=100:
#     while n!=0:
#         x = n%10
#         if x%2==0:
#             cntEven+=1
#         else:
#             cntOld+=1
#         n//=10
#     print(cntOld,end=' ')
#     print(cntEven)


           