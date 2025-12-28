def soThuanNghich(n):
    temp=n
    total=0
    while n>0:
        total = total*10 + n%10
        n//=10
    return temp==total
n=int(input())
if soThuanNghich(n):
    print("Số thuận nghịch")
else:
    print("Không phải số thuận nghịch")