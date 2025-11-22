N = int(input())

for i in range(N):
    for j in range(N):
        if(i==N//2 and j==N//2):
            print("X",end="")
        elif j==i:
            print("\\",end="")
        elif (i+j)+1==N:
            print('/',end="")    
        else:
            print("*",end="")    

        
    print()    