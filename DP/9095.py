n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

max_arr=max(arr)


dp=[0]*(max_arr+1)
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(4,max_arr+1):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

for i in range(n):
    print(dp[arr[i]])
