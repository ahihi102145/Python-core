# a,b= map(int,input().split())
# if a==0:
#     if b>0:
#         print("VSN")
#     else:
#         print("VN")
# else:
#     res= -b/a
#     if a>0:
#         print("x>{:.2f}".format(res))
#     else:
#         print("x<{:.2f}".format(res))
a,b= map(float,input().split())
if a==0:
    if b==0:
        print("VSN")
    else:
        print("VN")
else:
    print("{:.2f}".format(-b/a))