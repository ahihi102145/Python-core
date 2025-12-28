def digitIncreaseLeftToRight(n):
    if n<0:
        return "Error"
    s=str(n)
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return "No"
    return "Yes"
x,y,z=map(int,input().split())
print(digitIncreaseLeftToRight(x),digitIncreaseLeftToRight(y),digitIncreaseLeftToRight(z),end=" ")