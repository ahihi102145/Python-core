
str = input().strip()
words= str.split()
reslut = " ".join(w.capitalize() for w in words)
print(reslut)
