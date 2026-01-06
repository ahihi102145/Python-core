def hoanhao(n):
    total=1
    i=2
    while i*i<=n:
        if n%i==0:
            total=total+i*i