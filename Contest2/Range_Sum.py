T = int(input())

for i in range(T):
    L,R = map(int,input().split())
     
    if(L>R):
        L,R = R,L 
    sum_before_left = ((L - 1) * L) // 2
    sum_up_to_right = (R * (R + 1)) // 2

    Sum = sum_up_to_right-sum_before_left
    print(Sum)    

