N = int(input())
arr = list(map(int, input().split()))

Minimum = min(arr)
count = 0

for val in arr:
    if val == Minimum:
        count+=1

if(count%2!=0):
    print("Lucky")
else:
    print("Unlucky")    

