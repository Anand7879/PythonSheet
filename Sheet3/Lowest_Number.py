N = int(input())
T = list(map(int,input().split()))

lowest = T[0]
index = 1

for i in range(1,N):

    if(T[i]<lowest):
        lowest = T[i]
        index= i+1

print(lowest,index)
