def maxFreqInDigit(n):
    freq=[0]*10
    for c in n:
        freq[int(c)]+=1
    maxFreq=max(freq)
    for i in range(9,-1,-1):
        if freq[i]==maxFreq:
            return i
n=input()
print(maxFreqInDigit(n))