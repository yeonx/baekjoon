n=int(input())


for i in range(n):
    k=n-(i+1)
    for j in range(k):
        print(" ",end="")
    for j in range(i+1):
        if j==i:
            print("*")
        else:
            print("*",end="")
        
