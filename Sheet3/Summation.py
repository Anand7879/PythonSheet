N = int(input())
T = list(map(int,input().split()))
sum = 0

for i in range(N):
    sum+=T[i]

sum = abs(sum)
print(sum)