# def check_increase_digits(num):
#     if num <0:
#         return "Error"
#
#     s = str(num)
#     for i in range (len(s)-1):
#         if s[i] > s[i+1]:
#             return "No"
#     return "Yes"

def check_increase_digits(n):
    if n<0:
        return "Error"
    s = str(n)
    for i in range(len(s)-1):
        if s[i]> s[i +1]:
            return "No"
    return "Yes"
x, y, z = map(int, input().split())
print(check_increase_digits(x), check_increase_digits(y), check_increase_digits(z))

