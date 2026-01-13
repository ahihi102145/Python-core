n = input().strip()

if int(n) == 495:
    print(0)
else:
    steps = []

    while True:
        s = n.zfill(3)
        L = int("".join(sorted(s, reverse=True)))
        S = int("".join(sorted(s)))
        newN = L - S

        steps.append("{:03d} - {:03d} = {:03d}".format(L, S, newN))

        if newN == 495:
            break

        n = "{:03d}".format(newN)

    print(len(steps))
    for step in steps:
        print(step)
