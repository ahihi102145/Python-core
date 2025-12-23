def cnt_sum(n):
    sum1 = 0
    cnt =0

    while n > 0:
        sum1 += n % 10
        n //= 10
        cnt =cnt +1

    return cnt, sum1
a=int(input())
if a<0:
    print("Du lieu sai.")
else:
    s, c = cnt_sum(a)
    print(s, c)
