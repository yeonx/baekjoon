n=int(input())
dp=[0]*n
dp_re=[0]*n
arr=list(map(int,input().split()))

for i in range(n):
    m=0
    for j in range(i):
        if arr[i] > arr[j] and m < dp[j]:
            m=dp[j]
    dp[i]=m+1

for i in range(n):
    m=0
    for j in range(i):
        if arr[n-1-i] >arr[n-1-j] and m<dp_re[n-1-j]:
            m=dp_re[n-1-j]
    dp_re[n-1-i]=m+1

total=[0]*n
for i in range(n):
    total[i]=dp_re[i]+dp[i]-1
print(max(total))
