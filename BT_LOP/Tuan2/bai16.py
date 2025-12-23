s = input("Nhap cau :").strip()
if not s :
    print("Cau rong")
else:
    words=s.split()    
    cnt = len(words)
    print("So tu : {}".format(cnt))
