a,b,c = map(int, input("Nhập  3 cạnh tạm giác : ").split())
if a+b < c or a+c < b or b+c < a:
    print("Không phải tam giác")
else:
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")