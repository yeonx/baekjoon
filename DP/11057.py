n=int(input())

dp=[[0]*10 for _ in range(n+1)]

for i in range(10):
    dp[1][i]=i+1

for i in range(2,n+1):
    for j in range(10):
        for k in range(0,j+1):
            dp[i][j]+=dp[i-1][k]

print(dp[n][9]%10007)