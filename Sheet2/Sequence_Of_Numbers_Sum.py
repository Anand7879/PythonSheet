while True:
    N, M = map(int, input().split())

    if N <= 0 or M <= 0:
        break

    if N > M:
        N, M = M, N

    total = 0
    for i in range(N, M + 1):
        print(i, end=" ")
        total += i
    print(f"sum ={total}")
