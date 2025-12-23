#basic
# a,b = map(int, input().split())
# for i in range(a,b+1):
#     for j in range(1,10):
#             print("{}x{}={}".format(i,j,i*j))
#         print()

#advance

a,b = map(int, input().split())
for i in range(a,b+1):
    for j in range(i,10):
        print("{}x{}={}".format(i,j,i*j))
print()
