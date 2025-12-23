# def shh(n):
#
#     if n<2:
#         return 0
#     total = 1
#     for i in range(2,int(n**0.5)+1):
#         if n % i ==0:
#             total += i
#             if i!= n//i:
#                 total += n//i
#     return total==n

def shh(n):
    if n<2:
        return 0
    total =1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            total = total +i
            if i!= n//i:
                total += n//i
    return total==n
a,b= map(int, input().split())
stat = min (a,b)
end = max (a,b)
perfect_nums = []
for i in range(stat,end+1):
    if shh(i):
        perfect_nums.append(str(i))

if perfect_nums:
    print(" ".join(perfect_nums))
else:
    print("Khong co")

