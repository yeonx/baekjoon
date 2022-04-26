n=int(input())
dp=[0]*n
arr=list(map(int,input().split()))

for i in range(n):
    dp[i]=arr[i]
    m=0
    for j in range(i):
        if arr[j]<arr[i]:
            if dp[j]>m:
                m=dp[j]
    dp[i]+=m

print(max(dp))
