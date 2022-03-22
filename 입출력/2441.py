n=int(input())


for i in range(n):
    k=n-i
    for j in range(i):
        print(" ",end="")

    for j in range(k):
        if j==k-1:
            print("*")
        else:
            print("*",end="")
    
        
