N = int(input())

First = N//10
Second = N%10

if (First != 0 and Second % First == 0) or (Second != 0 and First % Second == 0):
    print("YES")
else:
    print("NO")