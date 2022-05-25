k=input()
n=[0 for _ in range(len(k)+1)]
for i in range(len(k)):
    n[i+1]=int(k[i])

dp=[0 for _ in range(len(n))]
N=len(n)
dp[0]=1

for i in range(1,N):
    if n[i]!=0:
        dp[i]=dp[i-1]+dp[i]
    
    x= int(n[i])+int(n[i-1])*10
    
    if (x>=10 and x<=26):
        dp[i]=dp[i-2]+dp[i]
        

print(dp[-1])
