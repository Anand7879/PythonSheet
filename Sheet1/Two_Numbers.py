# Given 2 numbers A and B
# Print floor, ceil and round of A/B
# Input
# Only one line containing two numbers A and B (1≤A,B≤103)

# Output
# Print 3 lines that contain the following in the same order:
# "floor A / B  = Floor result" without quotes.
# "ceil A / B = Ceil result" without quotes.
# "round A / B = Round result" without quotes.
import math
X,Y = map(int,input().split())
f = math.floor(X/Y)
c = math.ceil(X/Y)
r = math.floor(X/Y + 0.5)
print("floor " + str(X) + " / " + str(Y) + " = " + str(f))
print("ceil " + str(X) + " / " + str(Y) + " = " + str(c))
print("round " + str(X) + " / " + str(Y) + " = " + str(r))



