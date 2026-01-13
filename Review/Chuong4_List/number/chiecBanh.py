T, K = map(int, input().split())

banh = T // 5000

if banh == 0:
    print(0)
else:
    tong = banh + (banh - 1) // (K - 1)
    print(tong)
