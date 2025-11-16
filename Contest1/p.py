from itertools import permutations
a = [10,2,4]
op = ['+','-','*']
b = list(permutations(a))
c = list(permutations(op))

# print(b)
# print()
# print(c)

for num_perm in permutations(a):
     n1, n2, n3 = num_perm
     print(n1)
     print(n2)
     print(n3)

