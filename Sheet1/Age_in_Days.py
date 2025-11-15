X = int(input())
years = X // 365
months = (X % 365) // 30
days = (X % 365) % 30
print(f"{years} years")
print(f"{months} months")  
print(f"{days} days")
