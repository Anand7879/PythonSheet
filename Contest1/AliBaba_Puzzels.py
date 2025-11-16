from itertools import permutations

a, b, c, d = map(int, input().split())
nums = [a, b, c]
operators = ['+', '-', '*']

found = False

# We need ALL 3 operators used exactly once
for num_perm in permutations(nums):
    if found:
        break
    for op_perm in permutations(operators):  # All 3 operators
        n1, n2, n3 = num_perm
        op1, op2, op3 = op_perm
        
        # We have 3 numbers and 3 operators
        # Only 2 operators connect 3 numbers: n1 op1 n2 op2 n3
        # So we check if using op1 and op2 equals d
        # (op3 is just there to ensure all 3 are in the permutation)
        
        # Pattern 1: (n1 op1 n2) op2 n3
        if op1 == '+':
            result1 = n1 + n2
        elif op1 == '-':
            result1 = n1 - n2
        else:
            result1 = n1 * n2
            
        if op2 == '+':
            result1 = result1 + n3
        elif op2 == '-':
            result1 = result1 - n3
        else: 
            result1 = result1 * n3
            
        if result1 == d:
            found = True
            break
        
        # Pattern 2: n1 op1 (n2 op2 n3)
        if op2 == '+':
            result2 = n2 + n3
        elif op2 == '-':
            result2 = n2 - n3
        else: 
            result2 = n2 * n3
            
        if op1 == '+':
            result2 = n1 + result2
        elif op1 == '-':
            result2 = n1 - result2
        else:
            result2 = n1 * result2
                
        if result2 == d:
            found = True
            break

if found:
    print("YES")
else:
    print("NO")