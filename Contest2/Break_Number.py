x = int(input())
t = list(map(int,input().split()))
max = 0
count = 0
for num in t:
    count = 0
    while num%2==0 and num != 0:
        count+=1
        num = num//2

    if(count>max):
        max = count  
print(max)        

