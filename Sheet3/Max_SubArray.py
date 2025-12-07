T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    Max_list = []
    for j in range(N):
        max_val = arr[j]
        for k in range(j, N):
            if arr[k] > max_val:
                max_val = arr[k]
            Max_list.append(max_val)    
    print(' '.join(map(str, Max_list)))

