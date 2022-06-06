from collections import deque


n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

vis_dfs=[False]*(n+1)
vis_bfs=[False]*(n+1)


def dfs(v):
    vis_dfs[v]=True
    print(v,end=' ')
    
    for i in graph[v]:
        if not vis_dfs[i]:
            dfs(i)
def bfs(v):
    q=deque([v])
    vis_bfs[v]=True
    
    while q:
        k=q.popleft()
        print(k, end=' ')
        
        for i in graph[k]:
            if not vis_bfs[i]:
                q.append(i)
                vis_bfs[i]=True
    
dfs(v)
print()
bfs(v)
