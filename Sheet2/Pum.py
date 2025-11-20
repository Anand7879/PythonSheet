N = int(input())
count = N*4

for i in range(1,count+1):

    if(i%4==0):
        print("PUM")
    else:
        print(i,end=" ")
