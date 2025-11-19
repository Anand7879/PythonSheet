n,k,a = map(int,input().split())
product = n*k

if product%a!=0:
    print("double")
else:
    result = product // a

    Min_int = -2147483648
    Max_int = 2147483647

    if Min_int <= result <= Max_int:
        print("int")
    else:
        print("long long")