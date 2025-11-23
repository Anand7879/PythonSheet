N = int(input())
T = list(map(int,input().split()))
X = int(input())

if(T.__contains__(X)):
    index = T.index(X)
    print(index)
else:
    print(-1)    