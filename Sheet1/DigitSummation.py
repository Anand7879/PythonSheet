# Given two numbers N and M. Print the summation of their last digits.
# Input
# Only one line containing two numbers N, M (0 ≤ N, M ≤ 1018).
# Output
# Print the answer of the problem.

A,B = map(int,input().split())
last_digit_sum = (A % 10) + (B % 10)
print(last_digit_sum)