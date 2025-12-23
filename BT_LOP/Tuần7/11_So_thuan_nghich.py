def so_thuan_nghich(n):
    sum = 0
    temp = n
    while temp > 0: 
        digit =temp %10
        sum = sum *10 +digit
        temp = temp//10
    if n == sum:
        return "Số thuận nghịch"
    return "Không phải số thuận nghịch"

n = int(input("Nhập số nguyên dương n: "))
print(so_thuan_nghich(n))