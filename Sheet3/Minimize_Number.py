N = int(input())
arr = list(map(int,input().split()))
arr1 = []
count = 0
while(True):
    if(all ( x % 2==0 for x in arr)):
        arr = [x // 2 for x in arr]
        count+=1
    else:
        break

print(count)        
