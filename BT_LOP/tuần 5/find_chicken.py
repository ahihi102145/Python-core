x,d,m = map(int,input().split())
if m%(x*d)!=0:
    print(-1)
else:
    print(m//(x*d))    