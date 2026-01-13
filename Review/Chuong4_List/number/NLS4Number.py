'''
n = input().strip()

steps = []

while True:
    s = n.zfill(4)

    L = int("".join(sorted(s, reverse=True)))
    S = int("".join(sorted(s)))

    new_n = L - S

    steps.append("{:04d} - {:04d} = {:04d}".format(L, S, new_n))

    if new_n == int(s):
        n = "{:04d}".format(new_n)
        break

    n = "{:04d}".format(new_n)

print(n)
for step in steps:
    print(step)

'''
#6174
n=input().strip()
steps = []
while True:
    str=n.zfill(4)
    l = int("".join(sorted(str,reverse=True)))
    s=int("".join(sorted(str)))
    newN= l-s
    steps.append("{:04d} - {:04d} = {:04d}".format(l, s, newN))

    if newN == int(str):
        n="{:04d}".format(newN)
        break
    n= "{:04d}".format(newN)
print(n)
for step in steps:
    print(step)
# n=int(input())
# operation = []
# while True:
#     digits = []
#     tmp = n
#     while tmp > 0:
#         digits.append(tmp % 10)
#         tmp = tmp // 10
#     while len(digits) <4:
#         digits.append(0)
#     increseDigit = sorted(digits)
#     s = increseDigit[0] * 1000 + increseDigit[1] * 100 + increseDigit[2] * 10 + increseDigit[3]
#
#     decreseDigit = sorted(digits,reverse=True)
#     l = decreseDigit[0] * 1000 + decreseDigit[1] * 100 + decreseDigit[2] * 10 + decreseDigit[3]
#
#     newNumber = l-s
#     operation.append("{:04d} - {:04d} = {:04d}".format(l, s, newNumber))
#
#
#     if newNumber == n :
#         break
#
#     n=newNumber
# print(n)
# for op in operation:
#     print(op)
#
