n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
dp=[0 for _ in range(n)]

dp[0]=arr[0]
if (n>1):
    dp[1]=arr[0]+arr[1]
if(n>2):
    dp[2]=max(arr[0],arr[1])+arr[2]
if (n>3):
    for i in range(3,n):
        dp[i]=max(arr[i]+arr[i-1]+dp[i-3],arr[i]+dp[i-2])

print(dp[n-1])
