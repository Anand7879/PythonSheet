import math

X = int(input())
prime = True

if X <= 1:
    prime = False
else:
    for i in range(2, int(math.sqrt(X)) + 1):
        if X % i == 0:
            prime = False
            break

if prime:
    print("YES")
else:
    print("NO")
