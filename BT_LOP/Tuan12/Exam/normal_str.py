str=input().strip()
words= str.split()
res = " ".join(w.capitalize() for w in words)
print(res)