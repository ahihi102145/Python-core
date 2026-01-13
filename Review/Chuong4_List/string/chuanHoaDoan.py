import  re
#Cách truyền thống (không dùng thư viện nâng cao)
def chuan_hoa(s):
    def chuan_hoa(s):
        s = s.strip()
        result = ""
        can_viet_hoa = True
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isalpha():
                if can_viet_hoa:
                    result += ch.upper()
                    can_viet_hoa = False
                else:
                    result += ch.lower()

            elif ch == '.' or ch == ',':
                result += ch
                result += ' '
                can_viet_hoa = (ch == '.')
                # bỏ qua các dấu cách sau đó
                while i + 1 < len(s) and s[i + 1] == ' ':
                    i += 1

            elif ch == ' ':
                if result and result[-1] != ' ':
                    result += ' '

            else:
                result += ch

            i += 1

        return result
#Cách làm có dùng thư viện (re – regex)
def chuan_hoa2(s):
    s=s.strip().lower()
    # Chuẩn hóa dấu cách sau . và ,
    s= re.sub(r'\s*\.\s*','. ',s)
    s=re.sub(r'\s*,\s*',', ',s)
    s=re.sub(r'\s+',' ',s)
    result = ""
    viet_hoa = True

    for ch in s:
        if ch.isalpha() and viet_hoa:
            result += ch.upper()
            viet_hoa = False
        else:
            result += ch

        if ch == '.':
            viet_hoa = True

    return result

X = input().strip()
Y = input().strip()
print(chuan_hoa2(X))
print(chuan_hoa2(Y))
