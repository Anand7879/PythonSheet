T = int(input())

for _ in range(T):
    n,s = map(int,input().split())
    
    max_sum = n * (n + 1) // 2
    if s > max_sum:
        print(-1)
        continue

    ans = list()
    x = n
    while x>0 and s>0:

        if(x<=s):
            ans.append(x)
            s-=x

        x-=1
    if(s>0):
        print(-1)
    else:
        print(*ans)        
            
