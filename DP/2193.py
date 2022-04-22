
n=int(input())

dp=[0]*(n+1)

mul_num=1
add_num=0
for i in range(1,n+1):
    if i==1:
        dp[1]=1
    elif i==2:
        dp[2]=1
    elif i==3:
        dp[3]=2
    else:
        k=mul_num+add_num
        dp[i]=k*2 + (dp[i-1]-k)
        mul_num=k
        add_num=dp[i-1]-k

print(dp[n])
