n = int(input())
arr = list(map(int, input().split()))
K = int(input())
max_val = -1

for x in arr:
    if x <= K  and x > max_val:
        max_val = x

if max_val == -1:
        print("NO")
else:
    print(max_val)