mode = 10**9+7
def search_pass(s):
    total =1
    cur=""
    for c in s:
        if c.isdigit():
            cur+=c
        else:
            if cur!="":
                total = (total* int(cur))%mode
                cur=""
    if cur!="":
        total = (total* int(cur))%mode
    return total


s = input().strip()
print(search_pass(s))

