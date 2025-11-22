K,S = map(int,input().split())

count = 0
for x in range(max(0, S - 2*K), min(K, S) + 1):
    T = S - x  # Y + Z = T, need 0 <= Y, Z <= K
    count += min(K, T) - max(0, T - K) + 1

print(count)