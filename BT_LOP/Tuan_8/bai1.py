# def cnt_sum_digit (n):
#     sum=0
#     cnt=0
#
#     while n>0:
#         digit=n%10
#         sum+=digit
#         cnt+=1
#         n=n//10
#     return cnt,sum
def cnt_sum_digit(n):
    sum=0
    cnt =0
    while n>0:
        digit = n % 10
        sum += digit
        cnt += 1
        n //= 10
    return cnt,sum
n=int(input())
if n<0:
    print( "Du lieu sai.")
else:
    cnt,sum=cnt_sum_digit(n)
    print("{} {}".format(cnt,sum))