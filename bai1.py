def find_largest_odd_number(l, r):
    if not (0 <= l < r <= 10**9):
        raise ValueError("l va r phai thoa man 0 <= l < r <= 10**9")
    if r % 2 == 1: #Neu r la so le
        return max(l, r - 2), r #Tra ve so le lon nhat nho hon r va r
    elif r % 2 == 0 and r - 1 > l: #Neu r la so chan va r - 1 > l
        return max(l, r - 3), r - 1 #Tra ve so le lon nhat nho hon r - 1 va r - 1
    else:
        return -1, -1
#Input
l = int(input())
r = int(input())
try: #Output
    a, b = find_largest_odd_number(l, r)
    if a == -1:
        print(-1)
    else:
        print(a, b)
except ValueError as e:
    print(e)
