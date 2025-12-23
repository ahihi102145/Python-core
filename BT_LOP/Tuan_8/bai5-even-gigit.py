# def check_even_digits(n):
#     if n < 0:
#         return "Error"
#     s = str(n)
#     for ch in s:
#         if int(ch) % 2 != 0:
#             return "No"
#     return "Yes"


def check_even_digits(n):
    if n<0:
        return "Error"
    s=str(n)
    for ch in s:
        if int(ch)%2!=0:
            return "No"
    return "Yes"
x, y, z = map(int, input().split())

print(check_even_digits(x), check_even_digits(y), check_even_digits(z))
