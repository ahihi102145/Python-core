class sinhvien:
    def __init__(self, masv, ten,tuoi,diem=0.0):
        self.masv = masv
        self.ten = ten
        self.tuoi = tuoi
        self.diem = diem
    def add_point(self,diem):
        self.diem = diem

    def display(self):
        print(f"{self.masv:<10} {self.ten:<20} {self.tuoi:5} {self.diem:<5.2f}")
print(f"{'masv':<10}{'Hoten':<20}{'tuoi':<5}{'diem':<5}")

sv1=sinhvien(masv="SV01",ten="Nguyen van a",tuoi=5)
sv1.add_point(diem=10)
sv1.display()

sv2=sinhvien(masv="SV02",ten="Nguyen van B",tuoi=10)
sv2.add_point(diem=20)
sv2.display()
