a,b,c = map(int, input("Nhập  3 cạnh tạm giác : ").split())
if a+b < c or a+c < b or b+c < a:
    print("Không phải tam giác")
else:
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Diện tích tam giác là : ", s)    