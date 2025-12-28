data = list(map(int, input().split()))
n = data[0]

s = 0
for i in range(1, n + 1):
    s += data[i]

print(s)
