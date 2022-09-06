import sys

sys.setrecursionlimit(2000)

def dfs(now):
    if vis[now]==1:
        return
    else:
        vis[now]=1
        dfs(arr[now])

T = int(input())


for i in range(T):
    N = int(input())
    vis = []
    for j in range(N):
        vis.append(0)
    arr = []
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        arr[j]=arr[j]-1

    count =0 

    for j in range(N):
        if vis[j]== 0:
            dfs(j)
            count=count+1

    print(count)
