X,Y = input().split()

if float(X) > 0 and float(Y) > 0:
    print("Q1")
elif float(X) < 0 and float(Y) > 0:
    print("Q2")
elif float(X) < 0 and float(Y) < 0:
    print("Q3")
elif float(X) > 0 and float(Y) < 0:
    print("Q4")
elif float(X) == 0 and float(Y) != 0:
    print("Eixo Y")
elif float(Y) == 0 and float(X) != 0:
    print("Eixo X")    
elif float(X) == 0 and float(Y) == 0:
    print("Origem")
