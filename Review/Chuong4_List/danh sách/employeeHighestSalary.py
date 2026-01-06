n = int(input())
employee = []

for _ in range(n):
    info = input().split()
    ten = info[0]
    ma = int(info[1])
    hsl = float(info[2])
    pc = int(info[3])
    salary = hsl * 2000000 + pc
    employee.append((ma, ten, hsl, pc, salary))

res = max(employee, key=lambda x: x[4])

print("Nhan vien co luong lon nhat")
print("{} {} {:.2f} {} {:.2f}".format(res[0], res[1], res[2], res[3], res[4]))
