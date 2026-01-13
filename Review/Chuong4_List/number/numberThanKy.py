n=input().strip()
check=1
if int(n) %2 != 0:
    check=0
if '7' in n:
    check=0
tong=0
for ch in n:
    tong=tong+int(ch)
if tong %5!=0:
    check=0
if check==1:
    print("THAN KY")
else:
    print("KHONG THAN KY")

n = int(input())
temp = n
tong = 0
check = 1

if n % 2 != 0:
    check = 0

while temp > 0:
    d = temp % 10
    if d == 7:
        check = 0
    tong += d
    temp //= 10

if tong % 5 != 0:
    check = 0

if check == 1:
    print("THAN KY")
else:
    print("KHONG THAN KY")
