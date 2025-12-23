s = input().strip()
ops = ['+', '-', '*', '/', '%']
op = ''
for o in ops:
    if o in s:
        op = o
        break
if op == '':
    print("error")
else:
        x_str, y_str = s.split(op)
        x = int(x_str)
        y = int(y_str)

        if op == '+':
            print("{:.2f}".format(x + y))
        elif op == '-':
            print("{:.2f}".format(x - y))
        elif op == '*':
            print("{:.2f}".format(x * y))
        elif op == '/':
            if y == 0:
                print("error")
            else:
                print("{:.2f}".format(x / y))
        elif op == '%':
            if y == 0:
                print("error")
            else:
                print("{:.2f}".format(x % y))

