n, m, k = map(int, input().split())

count = 0

while k > 0:
    if n >= 1 and m >= 1:
        count += 1
        n -= 1
        m -= 1
        k -= 1

    elif n >= 2:
        count += 1
        n -= 2
        k -= 1

    else:
        break

print(count)
