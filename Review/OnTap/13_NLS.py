n=input().strip()
steps=[]

while True:
    str=n.zfill(4)
    l=int("".join(sorted(str,reverse=True)))
    s=int("".join(sorted(str)))
    nNew = l-s
    steps.append("{:04d} - {:04d} = {:04d}".format(l,s,nNew))

    if nNew==int(str):
        n="{:04d}".format(nNew)
        break
    n = "{:04d}".format(nNew)
print(n)
for step in steps:
    print(step)