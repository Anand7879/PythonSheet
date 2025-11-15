import math

a, b, c, d = map(int, input().split())

if a == 1 and c == 1:
    print("NO")  # 1^b = 1^d = 1, so not greater
elif a == 1:
    print("NO")  # 1^b = 1, c^d >= c >= 1, so not greater
elif c == 1:
    print("YES")  # a^b >= a >= 2, 1^d = 1, so greater
else:
    #  logarithms: a^b > c^d ⟺ b*log(a) > d*log(c)
    left = b * math.log(a)
    right = d * math.log(c)
    
    if left > right:
        print("YES")
    else:
        print("NO")