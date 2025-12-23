def max_in_digit(n):  
    max_digit = -1 
    if n<0:
        return "Error"
    while n > 0:
        digit = n%10 
        if digit > max_digit:
            max_digit = digit
        n = n//10
    return max_digit

x,y,z = map(int,input().split())
print(max_in_digit(x), end=' ')
print(max_in_digit(y),end=' ')
print(max_in_digit(z))