n=int(input())

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(2*n-1-2*i):
        if j==2*n-2-2*i:
            print("*")
        else:
            print("*",end="")

for i in range(1,n):
    for j in range(n-1-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j==2*i:
            print("*")
        else:
            print("*",end="")
