n = int(input())
# price =0
# if n == 1000 :
#     price = 1000
# elif 1000 <= n <= 25000:
#     price = 1000+ (n-1000)*13000
# elif 25000 <= n <=120000 :
#     price = 1000 +24000*13000+(n-25000)*11000
# else :
#     price = 1000 +24*13000+ 95000*11000 + (n-120000)*11000*0.01

# print(price)


for i in range(n):
    for j in range(n):
        if  j==0 or i==j or  j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ") 
    print()   