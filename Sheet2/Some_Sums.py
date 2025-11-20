N,A,B = map(int,input().split())
Sum = 0
for i in range(1,N+1):

    s = str(i)
    digit_sum = 0
    for ch in s:
        digit_sum=digit_sum+int(ch)
     
    if A<=digit_sum<=B:
        Sum+=i

print(Sum)

