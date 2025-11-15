a, b, k = map(int, input().split())

memo = (a % k == 0)
momo = (b % k == 0)

if memo and momo:
    print("Both")
elif memo:
    print("Memo")
elif momo:
    print("Momo")
else:
    print("No One")    