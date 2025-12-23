def check_gcd(a, b):
    if b==0:
        return a
    return check_gcd(b,a%b)

a,b,c = map(int, input().split())
if a<=0 or b<=0 or c<=0:
    print("Dữ liệu sai")
else:
    print(check_gcd(a,check_gcd(b,c)))