n = int(input())
values = list(map(int, input().split()))

Even_Count,Odd_count = 0,0
Positive_C,Negative_C = 0,0

for num in values:

    if num>0:
        Positive_C+=1
    elif num<0:
        Negative_C+=1 

    if num%2==0:
        Even_Count+=1
    else:
        Odd_count+=1


print(f"Even: {Even_Count}")
print(f"Odd: {Odd_count}")
print(f"Positive: {Positive_C}")
print(f"Negative: {Negative_C}")
