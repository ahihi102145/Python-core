n = int(input())

seen = set()  # lưu các giá trị đã xuất hiện để phát hiện vòng lặp

while True:
    if n == 1:
        print("HAPPY")
        break
    if n in seen:
        print("UNHAPPY")
        break
    seen.add(n)
    # tính tổng bình phương các chữ số
    n = sum(int(d) ** 2 for d in str(n))