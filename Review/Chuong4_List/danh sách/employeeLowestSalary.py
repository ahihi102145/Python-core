# n=int(input())

# minSalary = None
# res = None
# for _ in range(n):
#     info = input().split()
#     ma = int(info[0])
#     ten= info[1]
#     hsl = float(info[2])
#     pc = int(info[3])
#     salary = hsl * 2000000 + pc

#     if minSalary is None or  salary < minSalary:
#         minSalary=salary
#         res=(ma,ten,hsl,pc,salary)
# print("Nhan vien co luong thap nhat")
# print("{} {} {:.2f} {} {:.2f}".format(res[0],res[1],res[2],res[3],res[4]))

n=int(input())
employee = []
for _ in range(n):
    ma,ten,hsl,pc = input().split()
    ma=int(ma)
    hsl=float(hsl)
    pc=int(pc)
    salary = hsl * 2000000 + pc
    employee.append((ma,ten,hsl,pc,salary))

res = min(employee,key=lambda x:x[4])
print("Nhan vien co luong thap nhat")
print("{} {} {:.2f} {} {:.2f}".format(res[0], res[1], res[2], res[3], res[4]))
