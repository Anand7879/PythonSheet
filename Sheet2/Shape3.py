N = int(input())
S = "*"
temp = 0
for i in range(1,2*N+1):

    if(i<=N):
        spaces = N-i
        stars = 2*i-1
        print(" "*spaces,end="")
        print(S*stars)
    else:
        spaces = i-N-1
        stars = 2*(2*N-i)+1
        print(" "*spaces,end="")
        print(S*stars)
        temp+=1

        