n=int(input())
k=int(input())
total=0
for i in range(1,n+1):
    if i%k==0:
        #print(i)
        total+=i
print(total)