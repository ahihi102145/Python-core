def binary(num):
    bits  = []
    while num > 0:
        bits.append(str(num % 2))
        num = num // 2

    bits.reverse()
    return " ".join(bits)

a,b = map(int, input().split())
stat = min(a, b)
end = max(a, b)

for i in range(stat, end + 1):
    print("{}: {}".format(i, binary(i)))