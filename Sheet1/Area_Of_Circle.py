# Given a number R calculate the area of a circle using the following formula:
# Area = π * R2.
# Note: consider π = 3.141592653.
# Print the calculated area, with 9 digits after the decimal point.

R = float(input())
pi = 3.141592653

area = pi * R * R
print("%.9f" % area)


