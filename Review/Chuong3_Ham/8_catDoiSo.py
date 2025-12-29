def catDoi(s):
    res = ""
    for ch in s:
        if ch in "089":
            res+="0"
        elif ch == "1":
            res+="1"
        else:
            return "INVALID"
    res = res.lstrip('0')
    if res =="":
        return "INVALID"
    return res

t = int(input())
for _ in range(t):
    print(catDoi(input().strip()))