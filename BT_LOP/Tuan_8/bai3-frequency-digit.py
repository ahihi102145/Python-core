# # def frequent_digits(n):
# #     s = str(n)
# #     cnt = [0]*10
# #     for ch in s:
# #         cnt[int(ch)] += 1
# #     max_freq = max(cnt)
# #     for i in range(9,-1,-1):
# #         if cnt[i] == max_freq:
#             return i

# def frequent_digits(n):
#     s= str(n)
#     frequent = {}
#     for c in s:
#         if c in frequent:
#             frequent[c] += 1
#         else:
#             frequent[c] = 1
#     max_cnt=0
#     res=0
#     for c in frequent:
#         if frequent[c] > max_cnt:
#             max_cnt = frequent[c]
#             res = c
#         elif frequent[c] == max_cnt:
#             res = max(res,c)
#     return res

def frequent_digits(n):
    s=str(n)
    frequent= {}
    for c in s:
        if c in frequent:
            frequent[c] += 1
        else:
            frequent[c] = 1
    max_cnt =0
    res =0
    for c in frequent:
        if frequent[c] > max_cnt:
            max_cnt = frequent[c]
            res = c
        elif frequent[c] == max_cnt:
            res = max(res,c)
    return res




n=int(input())
print(frequent_digits(n))