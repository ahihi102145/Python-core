mod = 10**9+7
s=input().strip()
res=1
cur=0
found =0
for c in s:
    if c.isdigit():
        cur= cur*10+int(c)
        found=1
    else:
        if cur>0:
            res = (res*cur)%mod
            cur=0
if cur>0:
    res=(res*cur)%mod
print(res)

mod=10**9+7
s=input().strip()
nums=[]
tmp=""
for c in s:
    if c.isdigit():
        tmp+=c
    else:
        tmp+=" "
for x in tmp.split():
    nums.append(int(x))
res=1
for i in nums:
    res=(res*i)%mod
print(res)