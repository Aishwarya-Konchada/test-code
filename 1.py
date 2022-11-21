def Base3Num(num):
    if num == 0:
        return 0
    digits = ""
    while num:
        digits += str(num % 3)
        num //= 3
    return int(digits[::-1])

print(Base3Num(10))
