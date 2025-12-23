a,b,c= map (float,input().split())
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    print("Dien tich tam giac: {:.2f}".format(S))
    print("Chu vi tam giac: {:.2f}".format(a+b+c))
    
else:
    print("DL Sai")    

