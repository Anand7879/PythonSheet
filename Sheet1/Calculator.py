expression = input().strip()

# find the operator and split the expression
for op in ['+', '-', '*', '/']:
    if op in expression:
        S = op
        A, B = map(int, expression.split(op))
        break


if S == '+':
    print(int(A + B))
elif S == '-':
    print(int(A - B))
elif S == '*':
    print(int(A * B))
elif S == '/':
    print(int(A / B))