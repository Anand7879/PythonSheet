a, b, c, d = map(int, input().split())
product = a * b * c * d
last_two_digits = product % 100
print(f"{last_two_digits:02d}")