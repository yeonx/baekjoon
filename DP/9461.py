N=int(input())

for j in range(N):
    n=int(input())
    dp=[0 for _ in range(n+1)]
    
    for i in range(1,n+1):
        if i<=3:
            dp[i]=1
            continue
        dp[i]=dp[i-3]+dp[i-2]

    print(dp[n])
