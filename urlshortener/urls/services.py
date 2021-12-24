def from_base_10_to_64(num):
    digits = []
    while num > 0:
        remainder = num % 62
        digits.append(remainder)
        num = num // 62
    return digits
