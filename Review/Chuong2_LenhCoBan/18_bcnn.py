# def ucln(a,b):
#     while b:
#         a,b= b,a%b
#     return a
# def bcnn(a,b):
#     return a*b/ucln(a,b)

# a,b,c=map(int,input().split())
# if a>0 and b>0 and c>0:
#     print(int(ucln(a,ucln(b,c))))
# else:
#     print("DL sai.")

def ucln(a,b):
    while b:
        a,b= b,a%b
    return a
def bcnn(a,b):
    return a*b/ucln(a,b)

a,b=map(int,input().split())
if a>0 and b>0:
    print(int(bcnn(a,b)))
else:
    print("DL sai.")