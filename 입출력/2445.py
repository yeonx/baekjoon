n=int(input())


for i in range(n):
    for j in range(i+1):
        print("*",end="")
    for j in range((n-(i+1))*2):
        print(" ",end="")
    for j in range(i+1):
        if j==i:
            print("*")
        else:
            print("*",end="")

for i in range(1,n):
    for j in range(n-i):
        print("*",end="")
    for j in range(i*2):
        print(" ",end="")
    for j in range(n-i):
        if j==n-i-1:
            print("*")
        else:
            print("*",end="")
