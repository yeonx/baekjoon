n=int(input())

dp=[0 for _ in range(n+1)]
if(n>1):
    dp[0]=1
    dp[2]=3

for i in range(3,n+1):
    if i%2==1:
        continue
    dp[i]=dp[i-2]*3
    for j in range(0,i-3,2):
        dp[i]+=dp[j]*2

print(dp[n])
