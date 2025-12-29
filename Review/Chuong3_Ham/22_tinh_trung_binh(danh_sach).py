def tinh_trung_binh(danh_sach_str):
    nums=list(map(float,danh_sach_str.split()))
    return sum(nums)/len(nums)


s = input().strip()
print(tinh_trung_binh(s))
