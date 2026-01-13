# def drawSquare(h):
#     h = abs(h)
#     if h == 1:
#         print("*")
#         return
#     if h <= 0:
#         return
#     print("*" * h)
#     for _ in range(h - 2):
#         print("*" + " " * (h - 2) + "*")
#     print("*" * h)

# x, y, z = map(int, input().split())

# for v in (x, y, z):
#     print(v)
#     drawSquare(v)

def drawSquare(h):
    h=abs(h)
    if h==1:
        print("*")
        return
    if h<=0:
        return 0
    print("*" *h)
    for _ in range(h-2):
        print("*"+ " " * (h-2)+ "*")
    print("*" *h)
x,y,z=map(int,input().split())
for v in x,y,z:
    print(v)
    drawSquare(v)