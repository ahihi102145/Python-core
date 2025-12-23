n=int(input())
a=list(map(int,input().split()))
a.sort()
print("{}".format(n))
for i in a:
    print(i,end=' ')