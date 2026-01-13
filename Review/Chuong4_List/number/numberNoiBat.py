n=input().strip()
maxDigit=max(n)
cntMax=n.count(maxDigit)
if cntMax==1:
    print("NOI BAT")
else:
    print("KHONG NOI BAT")