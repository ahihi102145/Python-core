n=int(input())
year =2017
cnt=0
while cnt < n:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year,end=' ')
        cnt+=1
    year+=1