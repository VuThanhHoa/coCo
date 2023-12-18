def find_digit(k):
    # Kiểm tra điều kiện
    if not (1 <= k <= 10**9):
        raise ValueError("So nhap vao phai thoa man 1 <= k <= 10^9")

    # Tìm số chính phương mà chữ số thứ k nằm trong đó
    n = 1
    while k > len(str(n*n)): # Nếu k lớn hơn độ dài của n*n
        k -= len(str(n*n)) # Giảm k đi độ dài của n*n
        n += 1 # Tăng n lên 1

    # Tìm chữ số cụ thể
    return int(str(n*n)[k-1]) # Trả về chữ số thứ k trong n*n


# Input
k = int(input().strip())
try:
    print(find_digit(k))
except ValueError as e:
    print(e)
