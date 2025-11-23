K,S = map(int,input().split())
count = 0

for i in range(0,K):
    for j in range(0,K):
        for k in range(0,K):
            if(i+j+k==S):
                count+=1

print(count)