a,op,b=input()
a = int(a)
b = int(b)
if op=="+":
    print("{:.2f}".format(a+b))
elif op=="-":
    print("{:.2f}".format(a-b))
elif op=="*":
    print("{:.2f}".format(a*b))
if op=="/":
    if b!=0:
        print("{:.2f}".format(a/b))  
    else:
        print("Math error")
                     