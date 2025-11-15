A, S, B = input().split()
A = int(A)
B = int(B)

if S == '<':
    result = A < B
elif S == '>':
    result = A > B
elif S == '=':
    result = A == B

if result:
    print("Right")
else:
    print("Wrong")