n=int(input())

arr=[0]
dp=[0]*(n+1)
for i in range(n):
    arr.append(int(input()))

dp[1]=arr[1]
if n!=1:
    dp[2]=arr[1]+arr[2]

for i in range(3,n+1):
    dp[i]=max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2])
    dp[i]=max(dp[i],dp[i-1])

print(max(dp))
