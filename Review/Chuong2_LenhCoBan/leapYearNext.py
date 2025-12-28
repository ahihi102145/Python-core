n=int(input())
year= 2017
cnt=0
res=[]
while cnt<n:
    if year%4==0 and year%100!=0 or year%400==0:
        res.append(year)
        cnt=cnt+1
    year=year+1

print(*res)