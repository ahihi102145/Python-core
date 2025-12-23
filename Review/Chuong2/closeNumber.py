def closeNumber(a):
    total = 0
    for i in range(1,a):
        if a%i==0:
            if i == a:
                total = 0
            total+=i
    return total

a,b = map(int,input().split())

if a == closeNumber(b) and b==closeNumber(a):
    print("true")
else:
    print("false")