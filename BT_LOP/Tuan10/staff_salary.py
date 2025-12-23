n = int(input("Nhap so luong nhan vien : "))
salary_min = 1e9
name = ""
hsl_min = 0.0
tn_min = 0
for i in range(n):
    print(f"Nhan vien thu {i+1}:")
    ho_ten= input("Ho ten: ")
    hsl=float(input("He so luong: "))
    tham_nien=int(input("Tham nien cong tac: "))
    salary = hsl * 20000000 + tham_nien 
    if salary < salary_min:
        salary_min = salary
        name = ho_ten
        hsl_min = hsl
        tn_min = tham_nien

print("Nhan vien co luong thap nhat la: ")
print("Ho ten: ", name , ";He so luong: ", hsl_min , ";Tham nien cong tac: ", tn_min , ";Luong: ", salary_min)
