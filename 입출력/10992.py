n=int(input())

for i in range(n-1):
    for j in range(n-1-i):
        print(" ",end="")
    print("*",end="")
    for j in range(2*i-1):
        print(" ",end="")
    if i!=0:
        print("*")
    else:
        print("")

for i in range(2*n-1):
    print("*",end="")
