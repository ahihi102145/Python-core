f = open(r"D:\python_n04_2025\BT_LOP\Tuan 13\Open file\Dayso.txt", "r", encoding="utf-8")

print(f.readline())

lines = f.readline()
f.close()
res=0
for l in lines:
    num = l.split()
    for x in num:
        y = int(x)
        if y % 2 !=0:
            res = res + y
print("Tong cac so le trong tep {}".format(res))
