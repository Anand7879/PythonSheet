N = int(input())
arr = list(map(int, input().split()))

Max = max(arr)
Min = min(arr)

Max_Index = arr.index(Max)
Min_Index = arr.index(Min)

arr[Max_Index] , arr[Min_Index] = arr[Min_Index] ,  arr[Max_Index]

print(*arr)
