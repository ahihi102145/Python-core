def giaiThua(n):
    total =1
    for i in range(1,n+1):
        total*=i
    return total
n=int(input())
if n>=0:
    print(giaiThua(n))
else:
    print("Không tồn tại giai thừa cho số âm")