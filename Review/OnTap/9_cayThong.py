n=int(input())
wid=2*(n+2)-1
for h in [n,n+1,n+2]:
    for i in range(h):
        k=2*i+1
        sp=(wid-k)//2
        if k==1:
            print(" "*sp+"#")
        else:
            print(" "*sp+"#"+"x"*(k-2)+"#")