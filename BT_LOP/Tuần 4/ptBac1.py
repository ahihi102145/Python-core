#Giải bất phương trình ax+b>0
a,b = map(int,input().split())
if a==0:
    if b>0:
        print("VSN")
    else:
        print("VN")
elif a>0:
    print("x>{:.2f}".format(-b/a))
else:
    print("x<{:.2f}".format(-b/a))

#Viết chương trình giải phương trình (pt) ax+b=0.
# a,b = map(float,input().split())
# if a==0:
#     if b==0:
#         print("VSN")
#     else:
#         print("VN")
# else:
#     print("{:.2f}".format(-b/a))
