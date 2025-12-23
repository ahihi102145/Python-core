import  math
def snt(n):
    if n<=1:
        return 0
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return 0
    return 1

a,b = map(int,input().split())
lst = []
start = min(a, b)
end = max(a, b)
for i in range(start,end+1):
    if snt(i)==1:
        lst.append(i)

if len(lst)>0:
    print(*lst)
else:
    print("Khong co")