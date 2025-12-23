def nomalize_string(string):
    parts = string.strip().split()
    for i in range(len(parts)):
        parts[i] = parts[i].capitalize()
    return " ".join(parts)

n=(input("Enter string : "))
print(nomalize_string(n))