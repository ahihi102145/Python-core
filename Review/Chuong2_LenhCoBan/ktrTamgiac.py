import math

a, b, c = map(float, input().split())

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    chu_vi = a + b + c
    p = chu_vi / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))

    print("Dien tich tam giac: {:.2f}".format(dien_tich))
    print("Chu vi tam giac: {:.2f}".format(chu_vi))
else:
    print("DL Sai")
