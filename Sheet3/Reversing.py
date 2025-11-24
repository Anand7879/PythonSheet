N = int(input())
T = list(map(int,input().split()))

for i in range(N,0,-1):
    print(T[i-1],end=" ")