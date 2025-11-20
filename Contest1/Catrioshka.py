n, m, k = map(int, input().split())

useMouth = min(m,k,n)

n-=useMouth
m-=useMouth
k-=useMouth

useNoMouth = min(n//2,k)

print(useMouth+useNoMouth)