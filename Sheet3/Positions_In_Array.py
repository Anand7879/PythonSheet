N = int(input())
T = list(map(int,input().split()))

for i in range(N):
    if(T[i]<=10):
        print(f"A[{i}] = {T[i]}")
        