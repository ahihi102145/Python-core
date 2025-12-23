import  math

def calc(xa, ya, xb, yb):
    return math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)


xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
print(calc(xa, ya, xb, yb))