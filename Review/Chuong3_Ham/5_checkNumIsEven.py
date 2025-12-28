def check(n):
    if n<0:
        return "Error"
    else:
        while n>0:
            digit=n%10
            if digit%2!=0:
                return "No"
            n=n//10
        return "Yes"
a, b, c = map(int, input().split())
print(check(a), check(b), check(c))
