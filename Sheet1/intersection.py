l1, r1, l2, r2 = map(int, input().split())

# Find intersection boundaries
left = max(l1, l2)
right = min(r1, r2)

# Check if there is an intersection
if left <= right:
    print(left, right)
else:
    print(-1)