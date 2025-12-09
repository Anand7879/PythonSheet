# def fib(n):
#     if n==1 or n==2:
#         return n -1
    
#     result = fib(n-1) + fib(n-2)
#     return result

# print(fib(N))


N = int(input())

if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    a = 0
    b = 1
    for i in range(N-2):  
        a, b = b, a+b
    print(b)




