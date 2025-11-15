N = input().strip()

num = float(N)

if num == int(num):
    print("int", int(num))
else:
    integer_part = int(num)
    decimal_part = num - integer_part
    print(f"float {integer_part} {decimal_part:.3f}")