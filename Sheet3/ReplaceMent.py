N = int(input())
T = list(map(int,input().split()))

for i in range(N):
    if(T[i]>0):
        T[i]=1
    elif(T[i]<0):
        T[i] = 2

print(*T)
    