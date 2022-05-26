n= int(input())
p=list(map(int,input().split()))
dp=[0 for _ in range(n+1)]
for i in range(n):
    dp[i+1]=p[i]

for N in range(2,n+1):
    tmp=[]
    for i in range(1,N+1):
        if N%i==0:
            tmp.append(dp[i]*(N//i))
        elif i>N/2:
            tmp.append(dp[i]+dp[N-i])
    dp[N]=max(tmp)

print(dp[n])
