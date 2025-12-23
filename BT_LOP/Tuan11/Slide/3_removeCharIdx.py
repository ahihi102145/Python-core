def delete_char(word , idx):
    if idx < 0 or idx > len(word):
        return word
    return word[:idx] + word[idx+1:]
X = input()
n = int(input())
Y = input()
m = int(input())

X_result = delete_char(X, n)
Y_result = delete_char(Y, m)


print(X_result)
print(Y_result)