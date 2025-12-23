def armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_number = sum(int(digit)**num_digits for digit in num_str)
    return sum_number == n

n = int(input())
if armstrong(n):
    print(1)   
else:
    print(0)