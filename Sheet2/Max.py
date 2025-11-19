n = int(input())
values = list(map(int, input().split()))
Max = values[0]

for i in range(1,n):
    if(values[i]>Max):
        Max= values[i]

print(Max)