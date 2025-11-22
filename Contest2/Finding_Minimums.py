N,K = map(int,input().split())
T = list(map(int,input().split()))
L = list()
for i in range(0,len(T),K):
   end_index = i+K
   L = T[i:end_index]
   print(min(L),end=" ")