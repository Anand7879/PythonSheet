N = int(input())
T = list(map(int,input().split()))

lowest = T[0]
index = 1

for i in range(2,N+1):

    if(T[i]<lowest):
        lowest = T[i]
        index= i

print(lowest,index)
