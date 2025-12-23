n = int(input("Nhập số dòng n: "))

print("1. Tam giác vuông trái (đỉnh ở dưới):")
for i in range(1, n + 1):
    print("* " * i)

print("\n2. Tam giác vuông trái (đỉnh ở trên):")
for i in range(n, 0, -1):
    print("* " * i)

print("\n3. Tam giác vuông phải (đỉnh ở dưới):")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print("\n4. Tam giác cân (đỉnh ở trên):")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
