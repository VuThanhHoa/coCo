def max_sequences(l, r):
    # Kiểm tra điều kiện
    if not (1 <= l <= r <= 10**14):
        raise ValueError("So nhap vao phai thoa man 1 <= l <= r <= 10^14")

    max_length = 0
    count = 0

    for i in range(l, r + 1):
        length = 1
        current = i
        while current * 2 <= r: # Nhân với 2 để đảm bảo độ dài của dãy là lớn nhất, nếu nhân với 2 vượt quá r thì dừng.
            current *= 2
            length += 1

        if length > max_length:
            max_length = length
            count = 1
        elif length == max_length:
            count += 1

    return max_length, count

# Input
l = int(input())
r = int(input())

try:
    # Output
    result_length, result_count = max_sequences(l, r)
    print(result_length % 10**9, result_count % 10**9)
except ValueError as e:
    print(e)