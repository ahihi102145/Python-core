def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
k=int(input())
for i in range(k-1,1,-1):
    if prime(i):
        print(i)
        break