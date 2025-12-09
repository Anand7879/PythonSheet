N = int(input())
arr = list(map(int,input().split()))
arr1 = []
if(all ( x % 2==0 for x in arr)):
    arr = all ( x % 2==0 for x in arr)
    print(arr)
