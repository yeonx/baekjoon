n=int(input())

dis=list(map(int,input().split()))
cost=list(map(int,input().split()))

st=cost[0]

total=st*dis[0]

for i in range(1,n-1):
    if st>cost[i]:
        st=cost[i]
    total+=st*dis[i]
print(total)
