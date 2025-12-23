high , weight = map(int,input().split())
ibm = weight/high*high
if ibm <18.5:
    print("Bạn hơi gầy 1 tí")
elif ibm >=18.5 and ibm <=22.99:
    print("Thân hình bình thường")
elif ibm >23 and ibm <=25.99:
    print("Thừa cân")
else :
    print("Béo phì")