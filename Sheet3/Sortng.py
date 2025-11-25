N = int(input())
arr = list(map(int, input().split()))

for i in range(0,N):
    min_index = i
    
    for j in range(i+1,N):
        if(arr[j]<arr[min_index]):
            min_index = j
        
    if min_index != i:
        arr[min_index], arr[i] = arr[i], arr[min_index]

print(*arr)            



