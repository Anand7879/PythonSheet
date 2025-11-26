import sys
T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    smallest = sys.maxsize
    for j in range(N):
        for k in range(j+1,N):
            sum = arr[j]+arr[k]+(k+1)-(j+1)
            if(sum<smallest):
                smallest = sum
    print(smallest)            
    

