# def maxFreqInDigit(n):
#     freq=[0]*10
#     for c in n:
#         freq[int(c)]+=1
#     maxFreq=max(freq)
#     for i in range(9,-1,-1):
#         if freq[i]==maxFreq:
#             return i
# n=input()
# print(maxFreqInDigit(n))

# def he(n):
#     freq = [0]*10
#     while n!=0:
#         freq[n%10] +=1
#         n//=10
#     max_fre = max(freq)
#     for i in range(9,-1,-1):
#         if freq[i] == max_fre:
#             max_fre=freq[i]
#             return i
        
# n= int(input())
# print(he(n))       

# ap dung voi chu cai
def chu(s):
    freq=[0]*26
    for c in s:
        if c.isalpha():
            c=c.lower()
            freq[ord(c)- ord('a')] +=1
    max_fre = max(freq)
    for i in range(25,-1,-1):
        if freq[i] == max_fre:
            return chr(i+ord('a'))
        
print(chu("abcabc"))