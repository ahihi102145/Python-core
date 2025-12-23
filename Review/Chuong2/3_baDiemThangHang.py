def thang_hang(x1, y1, x2, y2, x3, y3):
    return abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) < 1e-9


x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())
x4, y4 = map(float, input().split())
x5, y5 = map(float, input().split())
x6, y6 = map(float, input().split())

res1 = "YES" if thang_hang(x1, y1, x2, y2, x3, y3) else "NO"
res2 = "YES" if thang_hang(x4, y4, x5, y5, x6, y6) else "NO"

print(res1, res2)
