import  math
def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1
K=int(input())
for i in range(K-1,1,-1):
     if prime(i):
         print(i)
         break