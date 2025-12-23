def list_odd_digits(n):
    if n < 0:
        print("Error")
        return
    s= str(n)
    result = []

    for ch in s:
        digit = int(ch)
        if digit % 2 != 0:     # số lẻ
            result.append(ch)

    if len(result) == 0:
        print("No")
    else:
        print(" ".join(result))


x, y, z = map(int, input().split())

list_odd_digits(x)
list_odd_digits(y)
list_odd_digits(z)
