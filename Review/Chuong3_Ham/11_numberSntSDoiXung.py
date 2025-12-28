def snt(n):
    if n<2:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

def SoDoiXung(n):
    temp=n
    total=0
    while n>0:
        total = total*10+ n%10
        n//=10
    # print(total)
    return temp==total

n=int(input())
if snt(n):
    print("Yes")
else:
    print("No")
if SoDoiXung(n):
    print("Yes")
else:
    print("No")