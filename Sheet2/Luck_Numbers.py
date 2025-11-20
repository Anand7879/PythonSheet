A, B = map(int, input().split())

found = False 

for i in range(A, B + 1):
    is_lucky = True
    s = str(i)
    for ch in s:
        if ch not in ('4', '7'):
            is_lucky = False
            break

    if is_lucky:
        print(i, end=" ")
        found = True

if not found:
    print(-1)
