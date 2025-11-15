X,Y,Z = map(int,(input().split()))
original = [X,Y,Z]

sorted_values = sorted([X, Y, Z])
for num in sorted_values:
    print(num)

print()

for num in original:
    print(num)



