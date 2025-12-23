n=input()
k=len(n)
s = sum(int(d)**k for d in n)

if s == int(n):
    print("1")
else:
    print("0")

