import sys
from collections import deque

input=sys.stdin.readline
N,M,V=map(int,input().split())

graph=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    
vis=[False]*(N+1)
def DFS(stand):
    vis[stand]=True
    print(stand,end=' ')
    for i in graph[stand]:
        if not vis[i]:
            DFS(i)


visit=[False]*(N+1)
def BFS(stand):
    q=deque([stand])
    visit[stand]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visit[i]:
                visit[i]=True
                q.append(i)
DFS(V)
print()
BFS(V)
