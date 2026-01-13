n=int(input())
tich=1
while n>0:
    digit=n%10
    if digit !=0:
        tich*=digit
    n//=10
print(tich)