T = int(input())

for _ in range(T):
    A,B = map(int,input().split())
    if(A>B):
        A,B = B,A
    OddSum = 0
    for i in range(A+1,B):
        if(i%2!=0):
            OddSum+=i
    print(OddSum)        

