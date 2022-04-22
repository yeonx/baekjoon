def find_max(col,arr):
    dp=[[0]*col for _ in range(2)]
    
    for i in range(col):
        for j in range(2):
            if i==0:
                dp[j][i]=arr[j][i]
            elif i==1:
                dp[j][i]=arr[j][i]+dp[(j+1)%2][i-1]
            else:
                dp[j][i]=max(dp[(j+1)%2][i-1],dp[(j+1)%2][i-2])+arr[j][i]
    return max(dp[0][col-1],dp[1][col-1])

n=int(input())
arr=[]

for i in range(n):
    arr[:]=[]

    col=int(input())

    for k in range(2):
        tmp=list(map(int,input().split()))
        arr.append(tmp)
    
    print(find_max(col,arr))
