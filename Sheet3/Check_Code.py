A,B = map(int,input().split())
S = input()

def check_digit(s,start,end):
    substring = s[start:end]
    return substring.isdigit()

if(S[A]=='-' and check_digit(S,0,A) and check_digit(S, A+1, len(S))):
    print("Yes")
else:
    print("No")
