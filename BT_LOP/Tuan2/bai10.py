import math
xa,ya,xb,yb = map(int,input().split())
kc = math.sqrt((xb-xa)*(xb-xa)+(yb-ya)*(yb-ya))
print("Do dai doan thang la:{:.2f}".format(kc))