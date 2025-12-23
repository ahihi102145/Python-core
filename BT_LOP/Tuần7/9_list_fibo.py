def list_fibo(n):
    fibo_list = []
    a,b=0,1
    for _ in range(n):
        fibo_list.append(b)
        a,b=b,a+b
    return fibo_list
n = int(input(""))
print(list_fibo(n))