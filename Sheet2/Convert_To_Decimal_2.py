T = int(input())

def Dec_To_Bin(n):
    if n == 0:
        return "0"
    
    s = ""
    while n>0:
        R = n%2
        n=n//2
        R = str(R)
        s=s+R
    
    s = s[::-1]
    return s   
       
def Bin_To_Dec(binary):
    value = 0
    for bit in binary:
        value = value * 2 + int(bit)
    return value       

for i in range(1,T+1):
    num = int(input())
    Binary = Dec_To_Bin(num)
    
    s= ""
    for ch in Binary:
        if ch in ["1"]:
            s+=ch
    
    print(Bin_To_Dec(s))


      




