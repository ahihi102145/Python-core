from django.template.defaultfilters import length


def check(num):
    if num<0:
        return "Error"
    s = str(num)
    for i in range(len(s)-1):
        if s[i]<s[i+1]:
            return "No"
        else:
            return "Yes"

x, y, z = map(int, input().split())
print(check(x), check(y), check(z))

