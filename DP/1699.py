n=int(input())

k=1

dp=[0 for _ in range(n+1)]
dp[1]=1

for i in range(2,n+1):
    if i==(k+1)*(k+1):
        k+=1
        dp[i]=1
        continue
    dp[i]=1+dp[i-k*k]
    if dp[i]==2:
        continue
    for j in range(1,k):
        dp[i]=min(dp[i],1+dp[i-j*j])

print(dp[n])
