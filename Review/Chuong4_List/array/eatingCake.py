n,k=map(int,input().split())
sumCake=n
vo=n
while vo>=k:
    doi=vo//k
    sumCake+=doi
    vo= vo%k+doi

print(sumCake)