x,d,m=map(int,input().split())
if m%(x*d)==0:
    print(int(m/(x*d)))
else:
    print('-1')