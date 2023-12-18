def max_number_after_removal(s):
    # Kiểm tra điều kiện
    if not (2 <= len(s) <= 10**5):
        raise ValueError("Chuoi nhap vao phai co toi thieu 2 va nhieu nhat 10^5 ky tu")

    # Loại bỏ chính xác một ký tự từ chuỗi
    s = list(s.lstrip('0'))  # Loại bỏ các số 0 không cần thiết ở đầu chuỗi, chuyển chuỗi thành list
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]: #Nếu ký tự đứng trước nhỏ hơn ký tự đứng sau
            del s[i] #Xóa ký tự đứng trước
            return int(''.join(s))  # Ép kiểu sang số nguyên
    del s[-1] # Nếu loop không return, xóa ký tự cuối cùng
    return int(''.join(s))  # Ép kiểu sang số nguyên

s = input().strip()
try:
    print(max_number_after_removal(s))
except ValueError as e:
    print(e)