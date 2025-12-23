n = int(input())
year= 2016
cnt =0
while cnt < n:
    year+=1
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year,end=" ")
        cnt += 1
