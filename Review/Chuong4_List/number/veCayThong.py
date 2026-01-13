
'''
1.h dong
-> in ra so ky tu : 2i +1
2.can giua tam giac
space = (maxWidth - (2*i+1)) // 2
maxwidth = 2(n+2)-1
3.in ra # va x
k==1 #
k>=3  # (k-2)*x # - > #x#
k=5 - > #xxx#
4.ghep 3 tang
h=n
h=n+1
h=n+2

'''
n=int(input())
maxWidth = 2*(n+2)-1
for h in [n,n+1,n+2]:
    for i in range(h):
        k=2*i+1
        space = (maxWidth-k) //2
        if k==1:
            print(" "*space+"#")
        else:
            print(" "*space+ "#" + "x"*(k-2) + "#")