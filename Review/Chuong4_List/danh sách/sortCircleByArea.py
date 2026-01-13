pi = 3.14159

n = int(input())
circle = []

for i in range(n):
    a = input().split()
    ma = int(a[0])
    x = int(a[1])
    y = int(a[2])
    r = float(a[3])
    area = pi * r * r
    circle.append((ma, x, y, r, area))

circle.sort(key=lambda x: x[4], reverse=True)
print("Danh sach hinh tron da sap xep:", n)
for c in circle:
    print("{} {} {} {:.3f}".format(c[0], c[1], c[2], c[3]))
