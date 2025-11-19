a, b, c, d = map(int, input().split())

List = list()
List.append(a+b-c)
List.append(a+b*c)
List.append(a-b+c)
List.append(a-b*c)
List.append(a*b+c)
List.append(a*b-c)

if List.__contains__(d):
    print("YES")
else:
    print("NO")