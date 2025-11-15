# Given 3 numbers A, B and C, Print the minimum and the maximum numbers.
# Input
# Only one line containing 3 numbers A, B and C ( - 105 ≤ A, B, C ≤ 105)
# Output
# Print the minimum number followed by a single space then print the maximum number.

A,B,C = map(int,input().split())
minimum = min(A,B,C)
maximum = max(A,B,C)

print(minimum,maximum)