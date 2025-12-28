# a,b= map(int,input().split())
# if a==0:
#     if b>0:
#         print("VSN")
#     else:
#         print("VN")
# else:
#     p = -b/a
#     if a > 0 :
#         print("x>{:.2f}".format(p))
#     else:
#         print("x<{:.2f}".format(p))

a,b= map(float,input().split())
if a==0:
    if b==0:
        print("VSN")
    else:
        print("VN")
else:
    print("{:.2f}".format(-b/a))