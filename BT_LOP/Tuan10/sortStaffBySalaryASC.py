"""
Viết chương trình nhập vào một danh sách gồm n nhân viên. Sắp xếp danh sách nhân viên theo lương tháng giảm dần và in kết quả ra màn hình.  Biết thông tin của một nhân viên gồm: tên nhân viên, mã nv, hệ số lương, phụ cấp. Lương tháng được tính bằng hệ số lương * 2000000 + phụ cấp.

Input: 

+ Dòng thứ nhất nhập vào n là số nhân viên

+ Dòng tiếp theo nhập vào thông tin của các nhân viên theo thứ tự tên, mã, hệ số lương, phụ cấp.

Output: 

+ Dòng thứ nhất in ra thông báo "Danh sach nhan vien da sap xep: n". Với n là số nhân viên trong danh sách.

+ Các dòng tiếp theo, mỗi dòng in ra thông tin của từng nhân viên. Các thông tin cách nhau dấu cách, thứ tự in ra là mã nhân viên, tên nhân viên, hệ số lương, phụ cấp, lương tháng. 

Constrains: 1<=n<=200, mã nhân viên, phụ cấp là các số nguyên dương, tên nhân viên không chứa dấu cách, các thông tin còn lại là số thực có độ chính xác 2 chữ số thập phân.


For example:

Input	Result
4
Anh 78 2.34 1000000
Vinh 5 3.3 500000
Nhung 61 2.67 700000
Trang 27 4.32 250000
Danh sach nhan vien da sap xep: 4
27 Trang 4.32 250000 8890000.00
5 Vinh 3.30 500000 7100000.00
61 Nhung 2.67 700000 6040000.00
78 Anh 2.34 1000000 5680000.00
"""
n=int(input())
lst =[]
for _ in range(n):
    info = input().split()
    ten = info[0]
    ma= info[1]
    hsl = float(info[2])
    pc = int(info[3])
    luong = hsl * 2000000 + pc
    lst.append(( ma,ten, hsl, pc, luong))
lst.sort(key=lambda x: x[4],reverse=True)
print("Danh sach nhan vien da sap xep: {}".format(n))
for staff in lst:
    print("{} {} {:.2f} {} {:.2f}".format(staff[0], staff[1], staff[2], staff[3], staff[4]))
