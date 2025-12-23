def sumUoc1(x):
    sum1=0
    for i in range(1,x):
        if x%i==0:
            sum1+=i
    return sum1

a,b=map(int,input().split())
sum1=sumUoc1(a)
sum2=sumUoc1(b)
if sum1 ==b and a == sum2:
    print("true")
else:
    print("false")

    