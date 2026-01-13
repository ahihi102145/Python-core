n,k=map(int,input().split())
a=list(map(int,input().split()))
fre=[0]*501
#fre[x] = số lần giá trị x đã xuất hiện trước đó
cnt=0
for i in range(n):
    #Duyệt từng phần tử a[i] từ trái sang phải
    res = k- a[i]*a[i]
    #Ta đang cố định i, muốn tìm j sao cho:
    if 0< res < 501:
        '''
fre[res] = số lần giá trị res đã xuất hiện trước đó
Mỗi lần xuất hiện tương ứng một cặp (j, i) hợp lệ
        '''
        cnt+=fre[res]
        #Xử lý trường hợp i = j
    if a[i] + a[i]*a[i] == k:
        cnt+=1
    #sau khi xử lý xong a[i], mới đưa vào fre
    fre[a[i]]+=1
print(cnt)