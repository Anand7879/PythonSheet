X,P = map(int,input().split())
discount_rate = X / 100
OriginalPrice = P/(1-discount_rate)
print(f"{OriginalPrice:.2f}")
