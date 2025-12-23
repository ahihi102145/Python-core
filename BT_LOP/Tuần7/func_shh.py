import  math
def shh(n):
    sum1 = 1
    if n<0 :
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum1 += i
            if i !=n//i:
                sum1 += n // i

    return sum1==n

a, b = map(int, input().split())
start = min(a, b)
end = max(a, b)

perfect_nums = []

for i in range(start, end + 1):
    if shh(i):
        perfect_nums.append(str(i))

if perfect_nums:
    print(" ".join(perfect_nums))
else:
    print("Khong co")

