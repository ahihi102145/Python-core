s=input().strip()
n=len(s)
def palin(t):
    return t ==t[::-1]

for i in range(n):
    if palin(s[i:]):
        add = s[:i][::-1]
        print(s+add)
        break
