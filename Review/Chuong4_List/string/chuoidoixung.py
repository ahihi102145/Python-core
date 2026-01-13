
def doixung(s):
    s=s.lower()
    return s==s[::-1]
s=input()
result=doixung(s)
if result:
    print("YES")
else:
    print("NO")