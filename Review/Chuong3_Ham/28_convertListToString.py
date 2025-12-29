def convertListToString(s):
    nums=list(map(int,s.split(",")))
    return ", ".join(map(str,nums))

s=input().strip()
print(convertListToString(s))